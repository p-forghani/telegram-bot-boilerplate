import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message
from loguru import logger

from .config import settings
from .handlers import register_handlers


async def start_bot():
    """Initialize and start the bot."""
    # Initialize bot and dispatcher
    bot = Bot(token=settings.BOT_TOKEN.get_secret_value())
    dp = Dispatcher()

    # Register all handlers
    register_handlers(dp)

    # Start polling
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


def main():
    """Entry point of the application."""
    # Configure logging
    logger.add(
        "logs/bot.log",
        rotation="500 MB",
        level=settings.LOG_LEVEL,
        format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}"
    )

    # Run the bot
    asyncio.run(start_bot())


if __name__ == "__main__":
    main() 