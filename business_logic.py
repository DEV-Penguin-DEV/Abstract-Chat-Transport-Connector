from http.client import HTTPException
import logging

from discord import Forbidden

from transports.discord import ChatTransportDiscord
from transports.telegram import ChatTransportTelegram

class SimpleBusinessLogic:
    """
    This class implements the business logic for handling messages from various transport layers.

    Attributes:
        transport (ChatTransport): The transport layer instance which handles specific platform communication.
    """

    def __init__(self, transport: ChatTransportDiscord | ChatTransportTelegram, logger: logging.Logger) -> None:
        """
        Initializes the business logic component with a specified transport.

        Args:
            transport (ChatTransport): An instance of a transport layer class that handles the messaging.
        """
        self.transport: ChatTransportDiscord | ChatTransportTelegram = transport
        self.logger: logging.Logger = logger
        # Add a message handler for incoming messages
        self.transport.add_handler('message', self.handle_message)

    async def handle_message(self, update, _context) -> None:
        """
        Handles incoming messages by extracting text and responding accordingly.

        Args:
            update (Any): The message update received from the transport. The type can vary depending on the transport used.

        Raises:
            Exception: Logs any exception that occurs during the message handling process.
        """
        try:
            # Extract the text from the message update based on platform specifics
            msg = self.transport.extract_message_text(update)
            self.logger.info(self.transport)
            # Generate a response message
            response = self.format_response(msg)
            chat_id = update.effective_chat.id  
            # Send the response message using the transport's method
            await self.transport.send_message(response, chat_id)
        except TimeoutError:
            self.logger.error("Timeout occurred while handling the message.")
        except HTTPException as http_err:
            self.logger.error(f"HTTP error occurred: {http_err}")
        except Forbidden:
            self.logger.error("Bot does not have the permission to send messages in this channel.")
        except Exception as e:
            # Общий перехватчик для всех непредвиденных исключений
            self.logger.error(f"An unexpected error occurred: {str(e)}")

    def format_response(self, message_text: str) -> str:
        """
        Formats a response message based on the input text. This method can be overridden to implement custom behavior.

        Args:
            message_text (str): The text received from the message to be responded to.

        Returns:
            str: A formatted response message.
        """
        return f"Hi! Your message was received: {message_text}"

    async def run(self):
        """
        Starts the transport to listen for and respond to messages asynchronously.
        """
        await self.transport.run()
