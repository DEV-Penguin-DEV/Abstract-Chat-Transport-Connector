import logging
import sys
import discord
from transports.chat_transport import ChatTransport

class ChatTransportDiscord(ChatTransport):
    """
    This class provides an implementation of the ChatTransport for Discord using the discord.py library.

    Attributes:
        client (discord.Client): The client instance for connecting to Discord.
        token (str): The authentication token used for logging in to Discord.
    """

    def __init__(self, token: str, logger: logging.Logger):
        """
        Initializes the Discord chat transport with necessary intents and token.

        Args:
            token (str): Discord bot token used for authentication.
        """
        self.logger: logging.Logger = logger
        intents = discord.Intents.default()
        intents.messages = True
        intents.message_content = True  # Required to access message content post-April 2022 changes.
        self.client = discord.Client(intents=intents)
        self.token = token
        
    def add_handler(self, event, handler):
        """
        Adds a handler function to the Discord client for a specific event type.

        Args:
            event (str): The type of event to handle (e.g., 'message').
            handler (Callable): The function that will handle the event.
        """
        if event == 'message':
            self.client.event(handler)

    async def run(self):
        """
        Starts the Discord client and listens for events such as when the bot is ready and when messages are received.
        """
        @self.client.event
        async def on_ready():
            self.logger.info(f'Logged in as {self.client.user}!')

        @self.client.event
        async def on_message(message):
            if message.author == self.client.user:
                return  # Avoids the bot responding to itself
            response = await self.handle_message(message)
            if response:
                await message.channel.send(response)

        try:
            await self.client.start(self.token)
        except discord.errors.LoginFailure:
            self.logger.error("Invalid token for Discord bot")
            sys.exit(1)

    async def send_message(self, msg: str, channel_id: int):
        """
        Sends a message to a specified channel.

        Args:
            msg (str): The message text to send.
            channel_id (int): The Discord channel ID where the message should be sent.

        Raises:
            Exception: Raises an exception if the channel could not be found.
        """
        channel = self.client.get_channel(channel_id)
        if channel:
            await channel.send(msg)
        else:
            self.logger.error(f"Could not find channel {channel_id}")
            sys.exit(1)

    def extract_message_text(self, update) -> str:
        """
        Extracts text from a message update.

        Args:
            update (discord.Message): The message update received.

        Returns:
            str: The text extracted from the message, or "No text found" if no text is available.
        """
        return update.content if update.content else "No text found"

    async def handle_message(self, message) -> str:
        """
        Handles an incoming message and determines the response.

        Args:
            message (discord.Message): The message received from Discord.

        Returns:
            str: A response message to be sent back to the channel.
        """
        text = self.extract_message_text(message)
        return f"Hi! Your message was received: {text}"
