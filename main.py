from aiogram import Bot, Dispatcher, F
from aiogram.filters.command import Command
from config import API_TOKEN

import asyncio

from bot.handlers import start

import logging

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot=bot)

dp.message.register(start, Command('start'))


if __name__ == "__main__":
    print("BOT STARTED")
    asyncio.run(dp.start_polling(bot)) 