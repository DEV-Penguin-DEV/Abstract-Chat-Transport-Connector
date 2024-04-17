import logging
from colorful_formatter import ColorfulFormatter
import os

def setup_logging():
    logger = logging.getLogger("MyApp")
    logger.setLevel(logging.DEBUG) 

    # Setup console logs
    console_handler = logging.StreamHandler()
    console_level = os.getenv('LOG_LEVEL_CONSOLE', 'INFO')
    console_handler.setLevel(console_level)
    console_formatter = ColorfulFormatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    console_handler.setFormatter(console_formatter)
    logger.addHandler(console_handler)

    # Setup files logs
    file_handler = logging.FileHandler('app.log')
    file_level = os.getenv('LOG_LEVEL_FILE', 'DEBUG')
    file_handler.setLevel(file_level)
    file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)

    return logger