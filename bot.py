import asyncio
import logging
from transports import ChatTransportDiscord, ChatTransportTelegram
from business_logic import SimpleBusinessLogic
import config
from colorama import Fore, Style, init
from logging_setup import setup_logging

logger = setup_logging()

init(autoreset=True)

async def main():
    logging.basicConfig(level=logging.INFO)
    # Select the transport based on configuration
    if config.USE_TELEGRAM:
        transport = ChatTransportTelegram(token=config.TELEGRAM_TOKEN, logger=logger)
        service_name = "Telegram"
    else:
        transport = ChatTransportDiscord(token=config.DISCORD_TOKEN, logger=logger)
        service_name = "Discord"
            
    bot = SimpleBusinessLogic(transport, logger)
    
    print(Fore.GREEN + f"{service_name} bot is now running!")
    print(Style.BRIGHT + Fore.CYAN + "Listening for messages...")
    

    await bot.run()

if __name__ == '__main__':
    asyncio.run(main())