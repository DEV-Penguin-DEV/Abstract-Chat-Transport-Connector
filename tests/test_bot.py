import logging
import unittest
from unittest.mock import Mock, patch
from transports import ChatTransportTelegram, ChatTransportDiscord
from business_logic import SimpleBusinessLogic
from colorful_formatter import ColorfulFormatter
from logging_setup import setup_logging


class TestChatTransports(unittest.IsolatedAsyncioTestCase):
    async def test_telegram_send_message(self):
        with patch('transports.ChatTransportTelegram.send_message') as mocked_send:
            transport = ChatTransportTelegram(token="dummy_token", logger=Mock())
            await transport.send_message("Hello, Telegram!")
            mocked_send.assert_called_once_with("Hello, Telegram!")

    async def test_discord_send_message(self):
        with patch('transports.ChatTransportDiscord.send_message') as mocked_send:
            transport = ChatTransportDiscord(token="dummy_token", logger=Mock())
            await transport.send_message("Hello, Discord!")
            mocked_send.assert_called_once_with("Hello, Discord!")

class TestSimpleBusinessLogic(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.mock_transport = Mock()
        self.mock_logger = Mock()
        self.logic = SimpleBusinessLogic(self.mock_transport, self.mock_logger)

    async def test_handle_message(self):
        update = {
            'message': 'test'
        }
        message = "Test message"
        context = Mock()
        await self.logic.handle_message(update, context)
        self.mock_transport.send_message(message, 1)
        
class TestLoggingSetup(unittest.TestCase):
    def test_logging_configuration(self):
        logger = setup_logging()
        self.assertEqual(logger.name, "MyApp")
        self.assertTrue(any(isinstance(h, logging.StreamHandler) for h in logger.handlers))
        self.assertTrue(any(isinstance(h.formatter, ColorfulFormatter) for h in logger.handlers))


if __name__ == '__main__':
    unittest.main()