import json
from dataclasses import dataclass

import requests


@dataclass
class NewCurrenc:
    data = requests.get("https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json").json()
    with open("lesson_09/data.json", "w") as outfile:
        json.dump(data, outfile)


# class Currency_Converter(NewCurrenc):
#     def __init__(
#         self,
#         another_currency,
#     ):
#         with open("lesson_09/data.json", "w") as outfile:
#             for el in outfile:
#                 if el["cc"] == another_currency:
#                     rate = el["rate"]
#                     return rate
#             raise Exception(f"The not currency")


if __name__ == "__main__":
    new_currency = NewCurrenc
    currency = input("Digit first currency: ").upper()
    # converter_1 = Currency_Converter(currency)
    # print(converter_1)
