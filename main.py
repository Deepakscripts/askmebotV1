import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from dotenv import load_dotenv
import os

from bot.handlers import main_router  # Use the combined router

load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    # Include combined router ONCE
    dp.include_router(main_router)

    # Optional: set commands for the bot
    await bot.set_my_commands([
        BotCommand(command="upload", description="Upload a PDF (only text)"),
        BotCommand(command="clear", description="Clear session memory"),
        BotCommand(command="help", description="Show help menu")
    ])

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
