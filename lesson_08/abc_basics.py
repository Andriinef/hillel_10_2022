from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def say_hello(self):
        raise NotImplementedError


class Dog(Animal):
    def say_hello(self):
        print("I am a dog")


class Cat(Animal):
    pass


jack = Dog()
jack.say_hello()


tom = Cat()  # type: ignore
# tom.say_hello()
