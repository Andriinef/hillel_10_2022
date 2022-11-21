from dataclasses import asdict, astuple, dataclass


class Price_:
    def __init__(self, amount: int, currency: str) -> None:
        self.amount: int = amount
        self.currency: str = currency

    def __str__(self) -> str:
        return f"amount = {self.amount}, currency = {self.currency}"


@dataclass
class Price:
    amount: int
    currency: str


price_ = Price_(40, "USD")
price = Price(30, "USD")
print(price_)
print(astuple(price))
print(asdict(price))
