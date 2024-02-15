from config import API_TOKEN_CONVERT
import requests

class ConvertService:

    @classmethod
    def convert(cls, amount, from_currency, to_currency):
        api_url = f"https://api.currencyapi.com/v3/latest?base_currency={from_currency}&currencies={to_currency}&apikey={API_TOKEN_CONVERT}"
        response = requests.get(api_url)
        data = response.json()['data']
        value = data[to_currency]['value']
        value = float(value)
        return value * amount
 

