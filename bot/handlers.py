from aiogram.types import Message
from aiogram import Bot

from bot.classes import BotAnswerClass

async def start(message: Message, bot: Bot):
    await message.delete()
    await message.answer(BotAnswerClass.start)

async def help(message: Message, bot: Bot):
    await message.delete()
    await message.answer(BotAnswerClass.help)
