import os
from bot import setup_bot

def main():
    # Get the token from environment variable
    # to set the token, run the command $env:DISCORD_TOKEN="your_bot_token_here" in the terminal
    TOKEN = os.getenv('DISCORD_TOKEN')
    if TOKEN is None:
        print("Please set the DISCORD_TOKEN environment variable")
        return

    print("Starting bot...")
    bot = setup_bot()
    bot.run(TOKEN)

if __name__ == "__main__":
    main()
