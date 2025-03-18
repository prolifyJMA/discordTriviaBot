# Import required libraries for Discord bot functionality, HTTP requests, and data management
import discord
from discord.ext import commands
import requests
import html
import random
from stats_manager import StatsManager

class TriviaBot(commands.Bot):
    def __init__(self):
        # Initialize Discord intents - these are required permissions for the bot to function
        intents = discord.Intents.default()
        intents.message_content = True  # Allows bot to read message content
        intents.members = True  # Allows bot to access member information
        intents.guilds = True  # Allows bot to access server information
        intents.guild_messages = True  # Allows bot to access server messages
        super().__init__(command_prefix="!", intents=intents)
        # Initialize the stats manager to track user statistics
        self.stats_manager = StatsManager()
        print("Bot initialized with intents:", intents)

    async def setup_hook(self):
        """Called when the bot is starting up, before it's ready"""
        print("Starting setup_hook...")
        # Print all registered commands for debugging purposes
        print("\nRegistered commands:")
        for command in self.tree.get_commands():
            print(f"- /{command.name}: {command.description}")

    async def on_ready(self):
        """Called when the bot has successfully connected to Discord"""
        print(f'Bot is ready! Logged in as {self.user}')
        print(f'Bot ID: {self.user.id}')
        print(f'Connected to {len(self.guilds)} guilds:')
        
        # Sync slash commands with Discord
        try:
            # First sync commands globally
            print("\nSyncing commands globally...")
            synced = await self.tree.sync()
            print(f"Successfully synced {len(synced)} command(s) globally")
            
            # Then sync commands to each individual server
            for guild in self.guilds:
                print(f'\nSyncing commands to guild: {guild.name}')
                try:
                    synced = await self.tree.sync(guild=guild)
                    print(f"Successfully synced {len(synced)} command(s) to {guild.name}")
                except Exception as e:
                    print(f"Failed to sync commands to {guild.name}: {e}")
        except Exception as e:
            print(f"Error syncing commands: {e}")
            print(f"Error type: {type(e)}")
            import traceback
            print(f"Traceback: {traceback.format_exc()}")

def get_trivia_question():
    """Fetches a random computer science trivia question from the OpenTDB API"""
    url = "https://opentdb.com/api.php?amount=1&category=18"  # Category 18 is Computer Science
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        if data["response_code"] == 0:  # 0 means successful response
            question_data = data["results"][0]
            # Decode HTML entities in the question and answers
            question = html.unescape(question_data["question"])
            correct_answer = html.unescape(question_data["correct_answer"])
            incorrect_answers = [html.unescape(ans) for ans in question_data["incorrect_answers"]]
            
            # Combine all answers and shuffle them for random order
            all_answers = [correct_answer] + incorrect_answers
            random.shuffle(all_answers)
            
            return {
                "question": question,
                "answers": all_answers,
                "correct_answer": correct_answer
            }
    except Exception as e:
        print(f"Error fetching trivia: {e}")
        return None

def setup_bot():
    """Sets up and configures all the bot's commands"""
    bot = TriviaBot()

    @bot.tree.command(name="trivia", description="Start a computer science trivia question")
    async def trivia(interaction: discord.Interaction):
        """Handles the /trivia command - displays a trivia question with multiple choice answers"""
        print(f"Trivia command triggered by {interaction.user.name}")
        trivia_data = get_trivia_question()
        if trivia_data:
            # Extract question data
            question = trivia_data["question"]
            answers = trivia_data["answers"]
            correct_answer = trivia_data["correct_answer"]
            
            # Format the question and answers with letters (A, B, C, D)
            message = f"```\n{question}\n\n"
            for i, answer in enumerate(answers):
                message += f"{chr(65+i)}. {answer}\n"  # 65 is ASCII for 'A'
            message += "```"
            
            # Create a view for the interactive buttons
            view = discord.ui.View()
            
            # Create a dictionary mapping letters to answers
            answer_dict = {chr(65+i): answer for i, answer in enumerate(answers)}
            
            # Create a button for each answer choice
            for letter in answer_dict:
                button = discord.ui.Button(label=letter, style=discord.ButtonStyle.blurple)
                
                async def button_callback(interaction: discord.Interaction, selected_letter=letter):
                    """Handles when a user clicks an answer button"""
                    selected_answer = answer_dict[selected_letter]
                    is_correct = selected_answer == correct_answer
                    
                    # Update the user's statistics
                    bot.stats_manager.update_stats(interaction.user.id, is_correct)
                    
                    # Create appropriate response message
                    if is_correct:
                        response = f"```\n{interaction.user.name} got it right! The answer was {selected_answer}!\n```"
                    else:
                        response = f"```\n{interaction.user.name} selected {selected_answer}... The correct answer was {correct_answer}!\n```"
                    
                    # Send response and disable all buttons
                    await interaction.response.send_message(response)
                    for item in view.children:
                        item.disabled = True
                    await interaction.message.edit(view=view)
                
                button.callback = lambda i, l=letter: button_callback(i, l)
                view.add_item(button)

            await interaction.response.send_message(message, view=view)
        else:
            await interaction.response.send_message("```\nSorry, I couldn't fetch a trivia question. Please try again.\n```")

    @bot.tree.command(name="stats", description="View trivia statistics for yourself or another user")
    async def stats(interaction: discord.Interaction, user: discord.Member = None):
        """Handles the /stats command - displays trivia statistics for a user"""
        # If no user is specified, show stats for the command user
        target_user = user or interaction.user
        stats_message = bot.stats_manager.format_stats_message(target_user.id, target_user.name)
        await interaction.response.send_message(f"```\n{stats_message}\n```")

    @bot.tree.command(name="leaderboard", description="View the trivia leaderboard")
    async def leaderboard(interaction: discord.Interaction):
        """Handles the /leaderboard command - displays rankings of all users by trivia performance"""
        print(f"Leaderboard command triggered by {interaction.user.name}")
        try:
            # Get all users who have played trivia
            user_ids = set(bot.stats_manager.stats.keys())
            print(f"Found {len(user_ids)} users in stats")
            
            # Create a mapping of user IDs to their Discord usernames
            user_names = {}
            for user_id in user_ids:
                try:
                    print(f"Fetching member info for user ID: {user_id}")
                    user = await interaction.guild.fetch_member(user_id)
                    user_names[user_id] = user.name
                    print(f"Successfully fetched user: {user.name}")
                except discord.NotFound:
                    print(f"User {user_id} not found in guild")
                    user_names[user_id] = f"User {user_id}"
                except discord.HTTPException as e:
                    print(f"HTTP error fetching user {user_id}: {e}")
                    user_names[user_id] = f"User {user_id}"
                except Exception as e:
                    print(f"Unexpected error fetching user {user_id}: {e}")
                    user_names[user_id] = f"User {user_id}"
            
            print(f"Successfully processed {len(user_names)} users")
            
            # Get and display the formatted leaderboard
            leaderboard_message = bot.stats_manager.format_leaderboard(user_names)
            print("Successfully formatted leaderboard message")
            await interaction.response.send_message(f"```\n{leaderboard_message}\n```")
            print("Successfully sent leaderboard message")
        except Exception as e:
            print(f"Error in leaderboard command: {e}")
            print(f"Error type: {type(e)}")
            import traceback
            print(f"Traceback: {traceback.format_exc()}")
            await interaction.response.send_message("```\nSorry, there was an error displaying the leaderboard. Please try again later.\n```")

    return bot 
