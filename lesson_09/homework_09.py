from dataclasses import dataclass

import requests


class CurrencyError(Exception):
    """Not valid currency"""


def update_currency_data_file():
    return requests.get("https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json").json()


def get_currensy_rate(currency, data):
    for el in data:
        if el["cc"] == currency:
            rate = el["rate"]
            return rate
    raise CurrencyError("The not currency")


@dataclass
class Price:
    amount: int
    currency: str

    def __add__(self, another_price):
        return Price(round(self.amount + another_price.amount, 2), self.currency)

    def __sub__(self, another_price):
        return Price(round(self.amount - another_price.amount, 2), self.currency)

    def __mul__(self, another_price):
        return Price(self.amount * another_price, "UAH")

    def __truediv__(self, another_price):
        return Price(self.amount / another_price, "USD")


if __name__ == "__main__":
    data = update_currency_data_file()
    amount = int(input("Digit first price: "))
    while True:
        currency = input("Enter first currency: ").upper()
        try:
            rate_first = get_currensy_rate(currency, data)
            break
        except CurrencyError:
            print("Currency does not exist")
    price_first = Price(amount, currency)

    amount = int(input("Digit second price: "))
    while True:
        currency = input("Entert second currency: ").upper()
        try:
            rate_does = get_currensy_rate(currency, data)
            break
        except CurrencyError:
            print("Currency does not exist")
    price_does = Price(amount, currency)
    if rate_first != rate_does:
        # """is a currency of the price that is on the left """
        #     price_does = price_does * rate_does
        #     price_does = price_does / rate_first
        """is a currency of the price USD"""
        rate_usb = get_currensy_rate("USD", data)
        if rate_first != rate_usb:
            price_first = price_first * rate_first
            price_first = price_first / rate_usb
        if rate_does != rate_usb:
            price_does = price_does * rate_does
            price_does = price_does / rate_usb
        print("-" * 30)
        print("Currencies of price instances are different. The price that is on the USD")
    add_price = price_first + price_does
    sub_price = price_first - price_does
    print(add_price)
    print(sub_price)
