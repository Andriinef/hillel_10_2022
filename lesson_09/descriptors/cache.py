from typing import Any


class Redis:
    storage: dict = {}

    def __set__(self, obj, value) -> None:
        raise Exception("You can not override the cache instance")

    def __get__(self, obj):
        return self

    @classmethod
    def set(cls, key: str, value: Any) -> None:
        cls.storage[key] = value

    @classmethod
    def get(cls, key: str) -> Any:
        return cls.storage.get(key, None)
