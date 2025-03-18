# Import required libraries for CSV file handling, operating system operations, and type hints
import csv
import os
from typing import Dict, Tuple, List

class StatsManager:
    """Manages the storage and retrieval of trivia game statistics for users"""
    
    def __init__(self, filename: str = "trivia_stats.csv"):
        """Initialize the stats manager with a CSV file for persistent storage"""
        self.filename = filename  # Name of the CSV file to store stats
        # Dictionary to store user stats in memory: user_id -> {trivias_answered, correct, incorrect}
        self.stats: Dict[int, Dict[str, int]] = {}
        self.load_stats()  # Load existing stats from file on startup

    def load_stats(self):
        """Load user statistics from the CSV file into memory"""
        if os.path.exists(self.filename):
            with open(self.filename, 'r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    # Convert user_id to integer and store their stats
                    user_id = int(row['user_id'])
                    self.stats[user_id] = {
                        'trivias_answered': int(row['trivias_answered']),
                        'correct': int(row['correct']),
                        'incorrect': int(row['incorrect'])
                    }

    def save_stats(self):
        """Save current statistics from memory to the CSV file"""
        with open(self.filename, 'w', newline='') as file:
            # Create CSV writer with appropriate column headers
            writer = csv.DictWriter(file, fieldnames=['user_id', 'trivias_answered', 'correct', 'incorrect'])
            writer.writeheader()
            # Write each user's stats to the file
            for user_id, stats in self.stats.items():
                writer.writerow({
                    'user_id': user_id,
                    'trivias_answered': stats['trivias_answered'],
                    'correct': stats['correct'],
                    'incorrect': stats['incorrect']
                })

    def update_stats(self, user_id: int, correct: bool):
        """Update a user's statistics after they answer a trivia question"""
        # Initialize stats for new users
        if user_id not in self.stats:
            self.stats[user_id] = {
                'trivias_answered': 0,
                'correct': 0,
                'incorrect': 0
            }
        
        # Increment total questions and correct/incorrect counts
        self.stats[user_id]['trivias_answered'] += 1
        if correct:
            self.stats[user_id]['correct'] += 1
        else:
            self.stats[user_id]['incorrect'] += 1
        
        # Save updated stats to file
        self.save_stats()

    def get_stats(self, user_id: int) -> Tuple[int, int, int, float]:
        """Retrieve a user's statistics including their success rate"""
        # Return zeros for users with no stats
        if user_id not in self.stats:
            return 0, 0, 0, 0.0
        
        stats = self.stats[user_id]
        total = stats['trivias_answered']
        if total == 0:
            return 0, 0, 0, 0.0
        
        # Calculate success rate as percentage
        ratio = (stats['correct'] / total) * 100
        return stats['trivias_answered'], stats['correct'], stats['incorrect'], ratio

    def format_stats_message(self, user_id: int, username: str) -> str:
        """Format a user's statistics into a readable message"""
        total, correct, incorrect, ratio = self.get_stats(user_id)
        if total == 0:
            return f"{username} hasn't answered any trivia questions yet!"
        
        # Create a formatted message with all stats
        return f"{username}'s Statistics:\n" \
               f"Total Questions: {total}\n" \
               f"Correct: {correct}\n" \
               f"Incorrect: {incorrect}\n" \
               f"Success Rate: {ratio:.1f}%"

    def get_leaderboard(self) -> List[Tuple[int, float, int, int, int]]:
        """Generate a sorted list of all users' statistics for the leaderboard"""
        leaderboard = []
        for user_id, stats in self.stats.items():
            total = stats['trivias_answered']
            if total > 0:  # Only include users who have played
                success_rate = (stats['correct'] / total) * 100
                # Add tuple of (user_id, success_rate, total, correct, incorrect)
                leaderboard.append((
                    user_id,
                    success_rate,
                    total,
                    stats['correct'],
                    stats['incorrect']
                ))
        
        # Sort by success rate (descending) and then by total questions (descending)
        return sorted(leaderboard, key=lambda x: (-x[1], -x[2]))

    def format_leaderboard(self, user_names: Dict[int, str]) -> str:
        """Format the leaderboard into a readable message with usernames"""
        leaderboard = self.get_leaderboard()
        if not leaderboard:
            return "No trivia statistics available yet!"
        
        # Create the leaderboard message with rankings
        message = "Trivia Leaderboard\n"
        for i, (user_id, success_rate, total, correct, incorrect) in enumerate(leaderboard, 1):
            username = user_names.get(user_id, f"User {user_id}")
            message += f"{i}. {username}\n"
            message += f"Success Rate: {success_rate:.1f}% | "
            message += f"Total: {total} | "
            message += f"Correct: {correct} | "
            message += f"Incorrect: {incorrect}\n"
        
        return message 
