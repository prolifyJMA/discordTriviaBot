# Import required libraries for CSV file handling, operating system operations, and type hints
import csv
import os
from typing import Dict, Tuple, List

class StatsManager:
    """Manages the storage and retrieval of trivia game statistics for users.
    
    This class handles all aspects of user statistics including:
    - Tracking total questions answered
    - Tracking correct and incorrect answers
    - Tracking hint usage
    - Calculating success rates
    - Generating leaderboards
    - Persistent storage in CSV format
    """
    
    def __init__(self, filename: str = "trivia_stats.csv"):
        """Initialize the stats manager with a CSV file for persistent storage.
        
        Args:
            filename (str): The name of the CSV file to store stats. Defaults to "trivia_stats.csv".
                          The file will be created if it doesn't exist.
        """
        self.filename = filename  # Name of the CSV file to store stats
        # Dictionary to store user stats in memory: user_id -> {trivias_answered, correct, incorrect, hints_used}
        self.stats: Dict[int, Dict[str, int]] = {}
        self.load_stats()  # Load existing stats from file on startup

    def load_stats(self):
        """Load user statistics from the CSV file into memory.
        
        This method reads the CSV file and populates the stats dictionary.
        If the file doesn't exist, it will be created when stats are first saved.
        The method handles backward compatibility by defaulting hints_used to 0
        for existing entries that don't have this field.
        """
        if os.path.exists(self.filename):
            with open(self.filename, 'r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    # Convert user_id to integer and store their stats
                    user_id = int(row['user_id'])
                    self.stats[user_id] = {
                        'trivias_answered': int(row['trivias_answered']),
                        'correct': int(row['correct']),
                        'incorrect': int(row['incorrect']),
                        'hints_used': int(row.get('hints_used', 0))  # Default to 0 if not present
                    }

    def save_stats(self):
        """Save current statistics from memory to the CSV file.
        
        This method writes all user statistics to the CSV file, creating it if it doesn't exist.
        The file includes columns for user_id, trivias_answered, correct, incorrect, and hints_used.
        """
        with open(self.filename, 'w', newline='') as file:
            # Create CSV writer with appropriate column headers
            writer = csv.DictWriter(file, fieldnames=['user_id', 'trivias_answered', 'correct', 'incorrect', 'hints_used'])
            writer.writeheader()
            # Write each user's stats to the file
            for user_id, stats in self.stats.items():
                writer.writerow({
                    'user_id': user_id,
                    'trivias_answered': stats['trivias_answered'],
                    'correct': stats['correct'],
                    'incorrect': stats['incorrect'],
                    'hints_used': stats['hints_used']
                })

    def update_stats(self, user_id: int, correct: bool):
        """Update a user's statistics after they answer a trivia question.
        
        Args:
            user_id (int): The Discord user ID of the player
            correct (bool): Whether the answer was correct or not
            
        This method:
        - Initializes stats for new users if needed
        - Increments the total questions counter
        - Updates correct/incorrect counters
        - Saves the updated stats to file
        """
        # Initialize stats for new users
        if user_id not in self.stats:
            self.stats[user_id] = {
                'trivias_answered': 0,
                'correct': 0,
                'incorrect': 0,
                'hints_used': 0
            }
        
        # Increment total questions and correct/incorrect counts
        self.stats[user_id]['trivias_answered'] += 1
        if correct:
            self.stats[user_id]['correct'] += 1
        else:
            self.stats[user_id]['incorrect'] += 1
        
        # Save updated stats to file
        self.save_stats()

    def increment_hints(self, user_id: int):
        """Increment the number of hints used by a user.
        
        Args:
            user_id (int): The Discord user ID of the player
            
        This method:
        - Initializes stats for new users if needed
        - Increments the hints_used counter
        - Saves the updated stats to file
        """
        # Initialize stats for new users
        if user_id not in self.stats:
            self.stats[user_id] = {
                'trivias_answered': 0,
                'correct': 0,
                'incorrect': 0,
                'hints_used': 0
            }
        
        # Increment hints used
        self.stats[user_id]['hints_used'] += 1
        
        # Save updated stats to file
        self.save_stats()

    def get_stats(self, user_id: int) -> Tuple[int, int, int, float, int]:
        """Retrieve a user's statistics including their success rate and hints used.
        
        Args:
            user_id (int): The Discord user ID of the player
            
        Returns:
            Tuple[int, int, int, float, int]: A tuple containing:
                - Total questions answered
                - Number of correct answers
                - Number of incorrect answers
                - Success rate as a percentage
                - Number of hints used
                
        Returns zeros for users with no stats or if they haven't answered any questions.
        """
        # Return zeros for users with no stats
        if user_id not in self.stats:
            return 0, 0, 0, 0.0, 0
        
        stats = self.stats[user_id]
        total = stats['trivias_answered']
        if total == 0:
            return 0, 0, 0, 0.0, 0
        
        # Calculate success rate as percentage
        ratio = (stats['correct'] / total) * 100
        return stats['trivias_answered'], stats['correct'], stats['incorrect'], ratio, stats['hints_used']

    def format_stats_message(self, user_id: int, username: str) -> str:
        """Format a user's statistics into a readable message.
        
        Args:
            user_id (int): The Discord user ID of the player
            username (str): The Discord username of the player
            
        Returns:
            str: A formatted message containing all user statistics including:
                - Total questions answered
                - Number of correct answers
                - Number of incorrect answers
                - Success rate as a percentage
                - Number of hints used
                
        Returns a message indicating no questions answered if the user has no stats.
        """
        total, correct, incorrect, ratio, hints = self.get_stats(user_id)
        if total == 0:
            return f"{username} hasn't answered any trivia questions yet!"
        
        # Create a formatted message with all stats
        return f"{username}'s Statistics:\n" \
               f"Total Questions: {total}\n" \
               f"Correct: {correct}\n" \
               f"Incorrect: {incorrect}\n" \
               f"Success Rate: {ratio:.1f}%\n" \
               f"Hints Used: {hints}"

    def get_leaderboard(self) -> List[Tuple[int, float, int, int, int, int]]:
        """Generate a sorted list of all users' statistics for the leaderboard.
        
        Returns:
            List[Tuple[int, float, int, int, int, int]]: A list of tuples containing:
                - User ID
                - Success rate as a percentage
                - Total questions answered
                - Number of correct answers
                - Number of incorrect answers
                - Number of hints used
                
        Only includes users who have answered at least 10 questions.
        The list is sorted by success rate (descending) and then by total questions (descending).
        """
        leaderboard = []
        for user_id, stats in self.stats.items():
            total = stats['trivias_answered']
            if total >= 10:  # Only include users who have answered at least 10 questions
                success_rate = (stats['correct'] / total) * 100
                # Add tuple of (user_id, success_rate, total, correct, incorrect, hints_used)
                leaderboard.append((
                    user_id,
                    success_rate,
                    total,
                    stats['correct'],
                    stats['incorrect'],
                    stats['hints_used']
                ))
        
        # Sort by success rate (descending) and then by total questions (descending)
        return sorted(leaderboard, key=lambda x: (-x[1], -x[2]))

    def format_leaderboard(self, user_names: Dict[int, str]) -> str:
        """Format the leaderboard into a readable message with usernames.
        
        Args:
            user_names (Dict[int, str]): A dictionary mapping user IDs to their Discord usernames
            
        Returns:
            str: A formatted message containing:
                - A header indicating the minimum question requirement
                - A ranked list of users with their statistics
                - Each user's entry includes:
                    - Rank
                    - Username
                    - Success rate
                    - Total questions
                    - Correct/incorrect counts
                    - Hints used
                    
        Returns a message indicating no qualifying users if no one has met the minimum question requirement.
        """
        leaderboard = self.get_leaderboard()
        if not leaderboard:
            return "No trivia statistics available yet! Answer at least 10 questions to appear on the leaderboard."
        
        # Create the leaderboard message with rankings
        message = "Trivia Leaderboard (Minimum 10 questions required)\n"
        for i, (user_id, success_rate, total, correct, incorrect, hints) in enumerate(leaderboard, 1):
            username = user_names.get(user_id, f"User {user_id}")
            message += f"{i}. {username}\n"
            message += f"Success Rate: {success_rate:.1f}% | "
            message += f"Total: {total} | "
            message += f"Correct: {correct} | "
            message += f"Incorrect: {incorrect} | "
            message += f"Hints: {hints}\n"
        
        return message 
