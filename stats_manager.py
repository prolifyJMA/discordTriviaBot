import csv
import os
from typing import Dict, Tuple

class StatsManager:
    def __init__(self, filename: str = "trivia_stats.csv"):
        self.filename = filename
        self.stats: Dict[int, Dict[str, int]] = {}  # user_id -> {trivias_answered, correct, incorrect}
        self.load_stats()

    def load_stats(self):
        """Load statistics from CSV file"""
        if os.path.exists(self.filename):
            with open(self.filename, 'r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    user_id = int(row['user_id'])
                    self.stats[user_id] = {
                        'trivias_answered': int(row['trivias_answered']),
                        'correct': int(row['correct']),
                        'incorrect': int(row['incorrect'])
                    }

    def save_stats(self):
        """Save statistics to CSV file"""
        with open(self.filename, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['user_id', 'trivias_answered', 'correct', 'incorrect'])
            writer.writeheader()
            for user_id, stats in self.stats.items():
                writer.writerow({
                    'user_id': user_id,
                    'trivias_answered': stats['trivias_answered'],
                    'correct': stats['correct'],
                    'incorrect': stats['incorrect']
                })

    def update_stats(self, user_id: int, correct: bool):
        """Update statistics for a user"""
        if user_id not in self.stats:
            self.stats[user_id] = {
                'trivias_answered': 0,
                'correct': 0,
                'incorrect': 0
            }
        
        self.stats[user_id]['trivias_answered'] += 1
        if correct:
            self.stats[user_id]['correct'] += 1
        else:
            self.stats[user_id]['incorrect'] += 1
        
        self.save_stats()

    def get_stats(self, user_id: int) -> Tuple[int, int, int, float]:
        """Get statistics for a user"""
        if user_id not in self.stats:
            return 0, 0, 0, 0.0
        
        stats = self.stats[user_id]
        total = stats['trivias_answered']
        if total == 0:
            return 0, 0, 0, 0.0
        
        ratio = (stats['correct'] / total) * 100
        return stats['trivias_answered'], stats['correct'], stats['incorrect'], ratio

    def format_stats_message(self, user_id: int, username: str) -> str:
        """Format statistics into a readable message"""
        total, correct, incorrect, ratio = self.get_stats(user_id)
        if total == 0:
            return f"**{username}** hasn't answered any trivia questions yet!"
        
        return f"**{username}**'s Statistics:\n" \
               f"Total Questions: {total}\n" \
               f"Correct: {correct}\n" \
               f"Incorrect: {incorrect}\n" \
               f"Success Rate: {ratio:.1f}%" 