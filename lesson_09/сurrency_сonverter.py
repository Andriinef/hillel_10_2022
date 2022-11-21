import json

import requests

currency = input("Digit first currency: ").upper()
data = requests.get("https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json").json()

with open("lesson_09/data.json", "w") as outfile:
    json.dump(data, outfile)
    for el in data:
        if el["cc"] == currency:
            print(el["rate"])

print(currency)
