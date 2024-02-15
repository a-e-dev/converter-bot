
class BotAnswerClass:

    start = """Привет! Я бот для конвертации валют. 
Используй команду /help, чтобы узнать доступные команды."""

    help = """Доступные команды:\n"
                 "/start - Начало работы\n"
                 "/help - Справка\n"
                 "/convert <amount> <from_currency> to <to_currency> - Конвертация валюты\n"
                 "Например: /convert 100 USD to EUR
    """

    uncorrect_convert = "Некорректный формат команды. Используйте /convert <amount> <from_currency> to <to_currency>"

    uncorrent_text = "Я не понимаю, что вы от меня хотите. Используйте /help для справки."