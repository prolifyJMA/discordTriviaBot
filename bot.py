import discord
from discord.ext import commands
import requests
import html
import random
from stats_manager import StatsManager

class TriviaBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True  # Enable message content intent
        intents.members = True  # Enable members intent
        super().__init__(command_prefix="!", intents=intents)
        self.stats_manager = StatsManager()

    async def setup_hook(self):
        # This is called when the bot starts up
        print('Syncing commands...')
        try:
            synced = await self.tree.sync()
            print(f"Synced {len(synced)} command(s)")
            
            print("\nAvailable commands:")
            for command in self.tree.get_commands():
                print(f"- /{command.name}: {command.description}")
        except Exception as e:
            print(f"Failed to sync commands: {e}")
            print("Trying to sync commands to current guild...")
            try:
                if self.guilds:
                    guild = self.guilds[0]
                    synced = await self.tree.sync(guild=guild)
                    print(f"Synced {len(synced)} command(s) to guild: {guild.name}")
                else:
                    print("Bot is not in any guilds!")
            except Exception as e:
                print(f"Failed to sync commands to guild: {e}")

    async def on_ready(self):
        print(f'Bot is ready! Logged in as {self.user}')
        print(f'Bot ID: {self.user.id}')

def get_trivia_question():
    url = "https://opentdb.com/api.php?amount=1&category=18"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        if data["response_code"] == 0:
            question_data = data["results"][0]
            question = html.unescape(question_data["question"])
            correct_answer = html.unescape(question_data["correct_answer"])
            incorrect_answers = [html.unescape(ans) for ans in question_data["incorrect_answers"]]
            
            # Combine and shuffle answers
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
    bot = TriviaBot()

    @bot.tree.command(name="trivia", description="Start a computer science trivia question")
    async def trivia(interaction: discord.Interaction):
        print(f"Trivia command triggered by {interaction.user.name}")
        trivia_data = get_trivia_question()
        if trivia_data:
            # Format the question and answers with letters
            question = trivia_data["question"]
            answers = trivia_data["answers"]
            correct_answer = trivia_data["correct_answer"]
            
            # Create the formatted message
            message = f"**{question}**\n\n"
            for i, answer in enumerate(answers):
                message += f"{chr(65+i)}. {answer}\n"  # 65 is ASCII for 'A'
            
            # Create buttons
            view = discord.ui.View()
            
            # Create a dictionary to store the answers
            answer_dict = {chr(65+i): answer for i, answer in enumerate(answers)}
            
            for letter in answer_dict:
                button = discord.ui.Button(label=letter, style=discord.ButtonStyle.blurple)
                
                async def button_callback(interaction: discord.Interaction, selected_letter=letter):
                    selected_answer = answer_dict[selected_letter]
                    is_correct = selected_answer == correct_answer
                    
                    # Update statistics
                    bot.stats_manager.update_stats(interaction.user.id, is_correct)
                    
                    # Create a response message
                    if is_correct:
                        response = f"🎉 **{interaction.user.name}** got it right! The answer was **{selected_answer}**!"
                    else:
                        response = f"❌ **{interaction.user.name}** selected **{selected_answer}**... The correct answer was **{correct_answer}**!"
                    
                    # Send the response to the channel
                    await interaction.response.send_message(response)
                    
                    # Disable all buttons after an answer is selected
                    view.disable_all_items()
                    await interaction.message.edit(view=view)
                
                button.callback = lambda i, l=letter: button_callback(i, l)
                view.add_item(button)

            await interaction.response.send_message(message, view=view)
        else:
            await interaction.response.send_message("Sorry, I couldn't fetch a trivia question. Please try again.")

    @bot.tree.command(name="stats", description="View your trivia statistics")
    async def stats(interaction: discord.Interaction):
        stats_message = bot.stats_manager.format_stats_message(interaction.user.id, interaction.user.name)
        await interaction.response.send_message(stats_message)

    return bot 