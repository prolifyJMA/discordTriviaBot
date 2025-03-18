# Import required libraries for environment variables, bot setup, and logging
import os
from bot import setup_bot
import logging

# Configure logging to display INFO level messages and above
# This will help with debugging and monitoring the bot's operation
logging.basicConfig(level=logging.INFO)

def main():
    """Main entry point for the Discord bot application"""
    # Get the Discord bot token from environment variables
    # This is a security best practice to avoid hardcoding sensitive information
    # To set the token, run: $env:DISCORD_TOKEN="your_bot_token_here" in PowerShell
    TOKEN = os.getenv('DISCORD_TOKEN')
    if TOKEN is None:
        logging.error("DISCORD_TOKEN environment variable is not set!")
        logging.info("Please run: $env:DISCORD_TOKEN=\"your_bot_token_here\"")
        return

    # Log startup information
    logging.info("Starting bot...")
    logging.info(f"Token length: {len(TOKEN)} characters")
    
    try:
        # Initialize and configure the bot
        logging.info("Setting up bot...")
        bot = setup_bot()
        logging.info("Bot setup complete")
        
        # Start the bot and connect to Discord
        logging.info("Attempting to run bot...")
        bot.run(TOKEN)
    except Exception as e:
        # Log any errors that occur during bot startup or operation
        logging.error(f"Error running bot: {e}")
        logging.error(f"Error type: {type(e)}")
        import traceback
        logging.error(f"Traceback: {traceback.format_exc()}")

# This ensures the main() function only runs if the script is executed directly
# (not when imported as a module)
if __name__ == "__main__":
    main()
