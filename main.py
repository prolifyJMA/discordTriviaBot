import os
from bot import setup_bot
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

def main():
    # Get the token from environment variable
    # to set the token, run the command $env:DISCORD_TOKEN="your_bot_token_here" in the terminal
    TOKEN = os.getenv('DISCORD_TOKEN')
    if TOKEN is None:
        logging.error("DISCORD_TOKEN environment variable is not set!")
        logging.info("Please run: $env:DISCORD_TOKEN=\"your_bot_token_here\"")
        return

    logging.info("Starting bot...")
    logging.info(f"Token length: {len(TOKEN)} characters")
    
    try:
        logging.info("Setting up bot...")
        bot = setup_bot()
        logging.info("Bot setup complete")
        
        logging.info("Attempting to run bot...")
        bot.run(TOKEN)
    except Exception as e:
        logging.error(f"Error running bot: {e}")
        logging.error(f"Error type: {type(e)}")
        import traceback
        logging.error(f"Traceback: {traceback.format_exc()}")

if __name__ == "__main__":
    main()
