import requests

currency = input("Digit first currency: ").upper()
data = requests.get("https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json").json()

for el in data:
    if el["cc"] == currency:
        print(el["rate"])
