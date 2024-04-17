from abc import ABC, abstractmethod

class ChatTransport(ABC):
    """
    Abstract base class defining the interface for different chat transport mechanisms.

    Methods defined here outline the basic capabilities that all derived chat transport classes should implement.
    """

    @abstractmethod
    def add_handler(self, event: str, handler) -> None:
        """
        Registers a handler for a specific type of event.

        Args:
            event (str): The type of event to handle, e.g., 'message'.
            handler: The function or coroutine that will be called when the event occurs.
        """
        pass

    @abstractmethod
    async def send_message(self, msg: str) -> None:
        """
        Sends a message to the chat service.

        Args:
            msg (str): The message text to send.
        """
        pass

    @abstractmethod
    def extract_message_text(self, update) -> str:
        """
        Extracts the text from a message update.

        Args:
            update: The message update received from the chat service. The exact type can vary between different services.

        Returns:
            str: The text extracted from the message update.
        """
        pass

    @abstractmethod
    async def run(self) -> None:
        """
        Starts the event loop for the chat transport, listening for incoming messages and handling them accordingly.
        """
        pass
