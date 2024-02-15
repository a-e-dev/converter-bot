from aiogram.types import Message
from aiogram import Bot

from bot.utils import BotAnswer
from bot.service import ConvertService

async def start(message: Message, bot: Bot):
    await message.delete()
    await message.answer(BotAnswer.START)

async def help(message: Message, bot: Bot):
    await message.delete()
    await message.answer(BotAnswer.HELP)

async def convert(message: Message, bot: Bot):
    try:
        _, amount, from_currency, _, to_currency = message.text.split()
        amount = float(amount)
        result = ConvertService.convert(amount, from_currency, to_currency)
        await message.answer(BotAnswer.get_convert_result(from_currency, to_currency, amount, result))
    except ValueError:
        await message.answer(BotAnswer.UNCORRENT_CONVERT)
    except KeyError:
        await message.answer(BotAnswer.UNCORRENT_CURRENCY)


async def other(message: Message):
    try:
        if "привет" in message.text.lower():
            await message.answer("Привет!")
        elif "пока" in message.text.lower():
            await message.answer("До свидания!")
        else:
            await message.answer("Я не понимаю, что вы от меня хотите. Используйте /help для справки.")
    except AttributeError:
        await message.answer("Я не понимаю, что вы от меня хотите. Используйте /help для справки.")


