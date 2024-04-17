import logging
from colorama import init, Fore, Style

init()  # initialization Colorama

class ColorfulFormatter(logging.Formatter):
    COLORS = {
        logging.DEBUG: Fore.BLUE + Style.NORMAL,
        logging.INFO: Fore.GREEN + Style.NORMAL,
        logging.WARNING: Fore.YELLOW + Style.NORMAL,
        logging.ERROR: Fore.RED + Style.NORMAL,
        logging.CRITICAL: Fore.RED + Style.BRIGHT,
    }

    def format(self, record):
        log_fmt = self.COLORS.get(record.levelno, Fore.WHITE) + self._fmt + Style.RESET_ALL
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)