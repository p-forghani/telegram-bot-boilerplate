# Telegram Bot Boilerplate

A modern Telegram bot boilerplate built with Aiogram 3.x, featuring a clean project structure and best practices.

## Features

- Modern project structure
- Type-safe configuration management with Pydantic
- Structured logging with Loguru
- Modular handler system
- Environment-based configuration
- Basic command handlers (/start, /help)

## Prerequisites

- Python 3.8+
- Telegram Bot Token (get it from [@BotFather](https://t.me/botfather))

## Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/telegram-bot-boilerplate.git
cd telegram-bot-boilerplate
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory:
```env
BOT_TOKEN=your_bot_token_here
LOG_LEVEL=INFO
```

## Running the Bot

To start the bot, run:
```bash
python -m src.bot
```

## Project Structure

```
telegram-bot-boilerplate/
├── src/
│   ├── __init__.py
│   ├── bot.py          # Main bot file
│   ├── config.py       # Configuration management
│   └── handlers.py     # Command and message handlers
├── logs/               # Log files directory
├── .env               # Environment variables
├── .gitignore
├── README.md
└── requirements.txt
```

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is licensed under the MIT License - see the LICENSE file for details.
