from aiogram import Bot, Dispatcher, F
from aiogram.filters.command import Command
from config import API_TOKEN_BOT

import asyncio

from bot.handlers import start, help, convert, other

import logging

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN_BOT)
dp = Dispatcher(bot=bot)

dp.message.register(start, Command('start'))
dp.message.register(help, Command('help'))
dp.message.register(convert, Command('convert'))
dp.message.register(other)


if __name__ == "__main__":
    print("BOT STARTED")
    asyncio.run(dp.start_polling(bot)) 