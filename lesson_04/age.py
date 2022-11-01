from typing import Generator, Iterable

data = [1, 2, 3, 4, 5, 1, 43, 5, 6, 2, 4, 1, 34, 45, 12, 4, 2]


class User:
    def __init__(self, username: str, age: int) -> None:
        self.username: str = username
        self.age: int = age

    def __repr__(self) -> str:
        return f"{self.username=}, {self.age}"


def only_adults(users: Iterable[User]) -> Generator:
    for user in users:
        if user.age > 18:
            yield user


# def get_list_without_duplicates(data: list) -> list:
#     values = set()
#     new_data: list = []

#     for element in data:
#         if element not in values:
#             values.add(element)
#             new_data.append(element)
#     return new_data


# for element in deduplication(data):
#     print(element)

# print(f"{data=}")
# print(f"{filtered=}")


john = User(username="John", age=22)
andrii = User(username="Andrii", age=45)
marry = User(username="Marry", age=8)

users = [john, andrii, marry]
# only_adults = (user for user in users if user.age > 18)

print(list(only_adults(users)))
