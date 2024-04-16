# Abstract Chat Transport Connector

This project provides a universal chat bot that can interface with both Discord and Telegram. The design allows for easy swapping between different chat platforms without altering the core business logic of the bot.

## Features

- Abstracted chat transport layer.
- Support for Discord and Telegram.
- Simple command response functionality.
- Easy to extend with more complex interactions.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the software and how to install them:
```bash
    python3 -m pip install discord.py python-telegram-bot
```
### Installing

A step-by-step series of examples that tell you how to get a development environment running:

1. **Clone the repository:**
```bash
    git clone git@github.com:DEV-Penguin-DEV/Abstract-Chat-Transport-Connector.git
    cd Abstract-Chat-Transport-Connector
```
2. **Set up environment variables:**

Create a `.env` file in the project root and add your bot tokens:

    DISCORD_TOKEN=your_discord_token_here
    TELEGRAM_TOKEN=your_telegram_token_here

3. **Run the bot:**
```bash
    python3 bot.py
```

## Project structure
```
├── bot.py                # Main script to run the bot
├── transports/           # Modules for different transports
│   ├── __init__.py       # Package initialization
│   ├── discord.py        # Module for Discord integration
│   └── telegram.py       # Module for Telegram integration
│
├── business_logic.py     # Bot's business logic
├── config.py             # Configuration for tokens and settings
├── requirements.txt      # Project dependencies
├── README.md             # Project description
├── .gitignore            # Git exclusions
└── tests/                # Tests for the project
    ├── __init__.py       # Test package initialization
    └── test_bot.py       # Tests for bot functionality
```

## Configuration

To switch between Discord and Telegram, modify the instantiation of the `SimpleBusinessLogic` object in your entry script:
```python
    from transports import ChatTransportDiscord, ChatTransportTelegram

    # For Discord
    transport = ChatTransportDiscord(token='your_discord_token_here')

    # For Telegram
    # transport = ChatTransportTelegram(token='your_telegram_token_here')

    bot = SimpleBusinessLogic(transport)
    bot.run()
```
## Running the tests

Explain how to run the automated tests for this system:
```bash
    python3 -m unittest discover -s tests
```
## Deployment

Add additional notes about how to deploy this on a live system.

## Built With

* [discord.py](https://discordpy.readthedocs.io/en/latest/) - The Discord API library
* [python-telegram-bot](https://python-telegram-bot.readthedocs.io/en/stable/) - The Telegram API library

## Authors

* **Konstantin Lysenko** - [DEV-Penguin-DEV](https://github.com/DEV-Penguin-DEV)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
