from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

# Fetching tokens from environment variables
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
USE_TELEGRAM = os.getenv('USE_TELEGRAM', 'false').lower() == 'true'