import asyncio
import logging
import sys
from telegram.ext import Application, MessageHandler, filters
from telegram.error import InvalidToken
from transports.chat_transport import ChatTransport

class ChatTransportTelegram(ChatTransport):
    """
    A ChatTransport implementation for handling Telegram messages using python-telegram-bot library.

    Attributes:
        application (Application): An instance of the Telegram bot Application.
    """

    def __init__(self, token: str, logger: logging.Logger):
        """
        Initializes the ChatTransportTelegram with a specific token for the Telegram bot.

        Args:
            token (str): The token used to authenticate the Telegram bot.
        """
        super().__init__()
        self.logger = logger
        self.application = Application.builder().token(token).build()
            

    def add_handler(self, event: str, handler) -> None:
        """
        Adds a message handler for a specific event type.

        Args:
            event (str): The type of event to handle, currently supports 'message'.
            handler (Callable): The function or coroutine that will be called when the event occurs.
        """
        if event == 'message':
            message_filter = filters.TEXT & ~filters.COMMAND
            self.application.add_handler(MessageHandler(message_filter, handler))

    async def send_message(self, msg: str, chat_id: int) -> None:
        """
        Asynchronously sends a message to a specified chat ID on Telegram.

        Args:
            msg (str): The message text to send.
            chat_id (int): The unique identifier for the target chat.
        """
        await self.application.bot.send_message(chat_id=chat_id, text=msg)
        
    def extract_message_text(self, update) -> str:
        """
        Extracts the text from a Telegram message update.

        Args:
            update: The update received from Telegram.

        Returns:
            str: The text extracted from the message update, or "No text found" if no text is available.
        """
        return update.message.text if update.message and update.message.text else "No text found"

    async def run(self) -> None:
        """
        Runs the event loop for the Telegram bot, processing messages as they arrive.
        """
        try:
            await self.application.initialize()
        except InvalidToken as e:
            self.logger.error(f"Invalid token provided for Telegram bot: {e}")
            sys.exit(1)
        
        offset = None
        while True:
            updates = await self.application.bot.get_updates(offset=offset, timeout=10)
            for update in updates:
                await self.application.process_update(update)
                offset = update.update_id + 1
            await asyncio.sleep(1)  # Pause to prevent hitting API limits
