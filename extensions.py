import requests
import json
from config import keys


class ConvertionException(Exception):
    pass

class CurrencyConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        if quote == base:
            raise ConvertionException(f"Невозможно перевести одинаковые валюты.")

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f"Не удалось обработать валюту {quote}")

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f"Не удалось обработать валюту {base}")

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f"Не удалось обработать количество {amount}")

        url = f"https://api.apilayer.com/currency_data/convert?to={base_ticker}&from={quote_ticker}&amount={amount}"
        headers = {
            "apikey": "vwAwPw2Tf3cyGHplfvc3UxQbzh7D5n4a"
        }
        response = requests.request("GET", url, headers=headers)
        text = response.json()
        status_code = response.status_code
        result = response.text
        t = json.loads(response.content)["result"]
        return t