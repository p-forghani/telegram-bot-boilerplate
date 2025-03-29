from aiogram import Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from loguru import logger


async def cmd_start(message: Message):
    """Handle /start command."""
    await message.answer(
        "👋 Welcome to the bot!\n\n"
        "This is a boilerplate Telegram bot built with Aiogram 3.x.\n"
        "Feel free to modify and extend it according to your needs."
    )
    logger.info(f"User {message.from_user.id} started the bot")


async def cmd_help(message: Message):
    """Handle /help command."""
    await message.answer(
        "🤖 Available commands:\n\n"
        "/start - Start the bot\n"
        "/help - Show this help message"
    )
    logger.info(f"User {message.from_user.id} requested help")


def register_handlers(dp: Dispatcher) -> None:
    """Register all handlers."""
    # Command handlers
    dp.message.register(cmd_start, Command("start"))
    dp.message.register(cmd_help, Command("help"))
    
    logger.info("Handlers registered successfully") 