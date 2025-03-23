# Import required libraries for Discord bot functionality, HTTP requests, and data management
import discord
from discord.ext import commands
import requests
import html
import random
from stats_manager import StatsManager
from trivia_questions import TRIVIA_QUESTIONS

class TriviaBot(commands.Bot):
    """A Discord bot that provides computer science trivia functionality.
    
    This bot implements the following features:
    - Interactive trivia questions with multiple choice answers
    - Hint system for questions
    - User statistics tracking
    - Leaderboard system
    - Persistent storage of user statistics
    """
    
    def __init__(self):
        """Initialize the Discord bot with required intents and components.
        
        Sets up the following intents:
        - message_content: Allows bot to read message content
        - members: Allows bot to access member information
        - guilds: Allows bot to access server information
        - guild_messages: Allows bot to access server messages
        
        Also initializes the stats manager for tracking user statistics.
        """
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
        """Called when the bot is starting up, before it's ready.
        
        This method:
        - Prints all registered slash commands for debugging purposes
        - Helps verify that all commands are properly registered
        """
        print("Starting setup_hook...")
        # Print all registered commands for debugging purposes
        print("\nRegistered commands:")
        for command in self.tree.get_commands():
            print(f"- /{command.name}: {command.description}")

    async def on_ready(self):
        """Called when the bot has successfully connected to Discord.
        
        This method:
        - Prints connection information
        - Syncs slash commands with Discord
        - Handles command syncing for both global and guild-specific commands
        - Includes error handling and logging for command syncing
        """
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

def get_trivia_question() -> dict:
    """Gets a random computer science trivia question from our custom database.
    
    Returns:
        dict: A dictionary containing:
            - question: The trivia question text
            - answers: A dictionary mapping letters (A-D) to answer choices
            - correct_answer: The letter corresponding to the correct answer
            - hint: A helpful hint for the question
            
    Returns None if there's an error fetching the question.
    The answers are randomly shuffled to prevent pattern recognition.
    """
    try:
        # Get a random question from our database
        question_data = random.choice(TRIVIA_QUESTIONS)
        
        # Format the question and answers
        question = question_data['question']
        correct_answer = question_data['correct_answer']
        incorrect_answers = question_data['incorrect_answers']
        hint = question_data['hint']
        
        # Combine all answers and shuffle them
        all_answers = [correct_answer] + incorrect_answers
        random.shuffle(all_answers)
        
        # Create answer mapping
        answer_mapping = {
            'A': all_answers[0],
            'B': all_answers[1],
            'C': all_answers[2],
            'D': all_answers[3]
        }
        
        # Find the correct answer letter
        correct_letter = next(letter for letter, answer in answer_mapping.items() 
                            if answer == correct_answer)
        
        return {
            'question': question,
            'answers': answer_mapping,
            'correct_answer': correct_letter,
            'hint': hint
        }
        
    except Exception as e:
        print(f"Error fetching trivia question: {e}")
        return None

def setup_bot():
    """Sets up and configures all the bot's commands.
    
    Returns:
        TriviaBot: The configured bot instance with all commands registered.
        
    This function sets up the following slash commands:
    - /trivia: Start a computer science trivia question
    - /stats: View trivia statistics for yourself or another user
    - /leaderboard: View the trivia leaderboard
    """
    bot = TriviaBot()

    @bot.tree.command(name="trivia", description="Start a computer science trivia question")
    async def trivia(interaction: discord.Interaction):
        """Handles the /trivia command - displays a trivia question with multiple choice answers.
        
        This command:
        - Fetches a random trivia question
        - Displays the question with multiple choice answers
        - Provides a hint button for users
        - Tracks user answers and updates statistics
        - Shows appropriate feedback messages
        
        The hint button is only visible to the user who clicked it.
        All buttons are disabled after an answer is selected.
        """
        print(f"Trivia command triggered by {interaction.user.name}")
        trivia_data = get_trivia_question()
        if trivia_data:
            # Extract question data
            question = trivia_data["question"]
            answers = trivia_data["answers"]
            correct_answer = trivia_data["correct_answer"]
            
            # Format the question and answers with letters (A, B, C, D)
            message = f"```\n{question}\n\n"
            for letter, answer in answers.items():
                message += f"{letter}. {answer}\n"
            message += "```"
            
            # Create a view for the interactive buttons
            view = discord.ui.View()
            
            # Create a dictionary mapping letters to answers
            answer_dict = {letter: answer for letter, answer in answers.items()}
            
            # Create a hint button
            hint_button = discord.ui.Button(label="Get Hint", style=discord.ButtonStyle.grey)
            
            async def hint_callback(interaction: discord.Interaction):
                """Handles when a user clicks the hint button.
                
                This callback:
                - Increments the user's hint count
                - Shows the hint as an ephemeral message (only visible to the user)
                """
                # Increment the user's hint count
                bot.stats_manager.increment_hints(interaction.user.id)
                
                # Get the hint from the trivia data
                hint = trivia_data["hint"]
                
                # Send the hint as an ephemeral message (only visible to the user who requested it)
                await interaction.response.send_message(f"```\nHint: {hint}\n```", ephemeral=True)
            
            hint_button.callback = hint_callback
            view.add_item(hint_button)
            
            # Create a button for each answer choice
            for letter in answer_dict:
                button = discord.ui.Button(label=letter, style=discord.ButtonStyle.blurple)
                
                async def button_callback(interaction: discord.Interaction, selected_letter=letter):
                    """Handles when a user clicks an answer button.
                    
                    This callback:
                    - Checks if the answer is correct
                    - Updates user statistics
                    - Shows appropriate feedback
                    - Disables all buttons after answering
                    """
                    selected_answer = answer_dict[selected_letter]
                    is_correct = selected_answer == correct_answer
                    
                    # Update the user's statistics
                    bot.stats_manager.update_stats(interaction.user.id, is_correct)
                    
                    # Create appropriate response message
                    if is_correct:
                        response = f"```\n{interaction.user.name} got it right! The answer was {selected_answer}!\n```"
                    else:
                        response = f"```\n{interaction.user.name} got it wrong... The correct answer was {answer_dict[correct_answer]}!\n```"
                    
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
        """Handles the /stats command - displays trivia statistics for a user.
        
        Args:
            interaction (discord.Interaction): The interaction that triggered the command
            user (discord.Member, optional): The user to show stats for. If None, shows stats for the command user.
            
        Shows statistics including:
        - Total questions answered
        - Correct/incorrect answers
        - Success rate
        - Hints used
        """
        # If no user is specified, show stats for the command user
        target_user = user or interaction.user
        stats_message = bot.stats_manager.format_stats_message(target_user.id, target_user.name)
        await interaction.response.send_message(f"```\n{stats_message}\n```")

    @bot.tree.command(name="leaderboard", description="View the trivia leaderboard")
    async def leaderboard(interaction: discord.Interaction):
        """Handles the /leaderboard command - displays rankings of all users by trivia performance.
        
        Args:
            interaction (discord.Interaction): The interaction that triggered the command
            
        Features:
        - Only shows users who have answered at least 10 questions
        - Sorts users by success rate and total questions
        - Shows comprehensive statistics for each user
        - Handles errors gracefully with appropriate error messages
        
        The leaderboard includes:
        - User rankings
        - Success rates
        - Total questions answered
        - Correct/incorrect counts
        - Hints used
        """
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
