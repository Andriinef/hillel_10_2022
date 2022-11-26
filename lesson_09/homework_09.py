from dataclasses import dataclass

import requests


class CurrencyError(Exception):
    """Not valid currency"""


def update_currency_data_file():
    return requests.get("https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json").json()


def get_input_validation(item):
    while True:
        currency = input(f"Enter {item} currency: ").upper()
        try:
            rate = [el["rate"] for el in data if el["cc"] == currency]
            return currency, float(rate[0])
        except CurrencyError:
            print("Currency does not exist")


def get_currensy_rate(currency, data):
    rate = [el["rate"] for el in data if el["cc"] == currency]
    return float(rate[0])


@dataclass
class Price:
    amount: int
    currency: str

    def __add__(self, another_price):
        return Price(round(self.amount + another_price.amount, 2), self.currency)

    def __sub__(self, another_price):
        return Price(round(self.amount - another_price.amount, 2), self.currency)

    def __mul__(self, another_price):
        if self.currency != "USD":
            return Price(self.amount * another_price, "UAH")
        else:
            return Price(self.amount, self.currency)

    def __truediv__(self, another_price):
        if self.currency != "USD":
            return Price(self.amount / another_price, "USD")
        else:
            return Price(self.amount, self.currency)


if __name__ == "__main__":
    data = update_currency_data_file()
    amount = int(input("Digit first price: "))
    price = get_input_validation("first")
    rate_first = price[1]
    price_first = Price(amount, price[0])

    amount = int(input("Digit second price: "))
    price = get_input_validation("does")
    rate_does = price[1]
    price_does = Price(amount, price[0])

    if rate_first != rate_does:
        """is a currency of the price USD"""
        rate_usb = get_currensy_rate("USD", data)
        price_first = price_first * rate_first
        price_first = price_first / rate_usb
        price_does = price_does * rate_does
        price_does = price_does / rate_usb
        # """is a currency of the price that is on the left """
        #     price_does = price_does * rate_does
        #     price_does = price_does / rate_first
        print("-" * 30)
        print("Currencies of price instances are different. The price that is on the USD")
    add_price = price_first + price_does
    sub_price = price_first - price_does
    print(add_price)
    print(sub_price)
