class BotAnswer:
    START = "Привет! Я бот для конвертации валют.\nИспользуй команду /help, чтобы узнать доступные команды."

    HELP = ("Доступные команды:\n"
                    "/start - Начало работы\n"
                    "/help - Справка\n"
                    "/convert <amount> <from_currency> to <to_currency> - Конвертация валюты\n"
                    "Например: /convert 100 USD to EUR")

    UNCORRENT_CONVERT = "Некорректный формат команды. Используйте /convert <amount> <from_currency> to <to_currency>"
    
    UNCORRENT_CURRENCY = "Неверныый формат одной из валют!"

    UNCORRENT_TEXT = "Я не понимаю, что вы от меня хотите. Используйте /help для справки."

    @classmethod
    def get_convert_result(cls, from_currency, to_currency, amount, result):
        return f"{amount} {from_currency} == {result} {to_currency}"