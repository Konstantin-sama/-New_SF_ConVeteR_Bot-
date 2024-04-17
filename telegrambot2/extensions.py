import requests
import json
from config import exchanges

class APIException(Exception):
    pass
class Converter:
    @staticmethod
    def get_price(base, sym, amount):
        try:
            base_key = exchanges[base.lower()]
        except KeyError:
            raise APIException(f'Валюта  {base} не найдена!')

        try:
            sym_key = exchanges[sym.lower()]
        except KeyError:
            raise APIException(f'Валюта  {sym} не найдена!')
        if base_key == sym_key:
            raise APIException(f'Невозможно перевести одинаковые валюты {base}!')

        try:
            amount = float(amount.replace(',', '.'))
        except ValueError:
            raise APIException(f'не удалось обработать количество {amount}!')


        r = requests.get(f'https://v6.exchangerate-api.com/v6/???/latests/USD?base={base_key}&symbols={sym_key}')
        resp = json.loads(r.content)
        new_price = resp['conversion_rates'][sym_key] * amount
        new_price = round(new_price, 3)
        message = f'Цена {amount} {base} в {sym} : {new_price}'
        return message
