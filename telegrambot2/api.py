import requests
import json
base_key = 'USD'
sym_key = 'RUB'
amount = 100

r = requests.get(f"https://v6.exchangerate-api.com/v6/724c336b0f189189de0edf6b/latests/USD?base={base_key}&symbols={sym_key}")
# print(r.content)
resp = json.loads(r.content)
# print(resp)
new_price = resp["conversion_rates"][sym_key] * amount

# print(new_price)