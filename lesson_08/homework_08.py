from abc import ABC, abstractclassmethod
from itertools import chain
from random import choice


class Shape(ABC):
    @abstractclassmethod
    def draw(self):
        pass


class Rectangle(Shape):
    def draw(self):
        print("---- \n|  |\n----")


class Circle(Shape):
    def draw(self):
        print("  --\n -  -\n  --")


class Square(Shape):
    def draw(self):
        print("\n".join("* " * 4 for i in range(4)))


class Spruce(Shape):
    def draw(self):
        print(
            "\n".join(
                chain(
                    (("* " * i + "*").rjust(7 * 2 + i) for i in range(5)),
                    (("* " * i + "*").rjust(7 * 2 + i) for i in range(1, 7)),
                    (("* " * i + "*").rjust(7 * 2 + i) for i in range(1, 9)),
                )
            )
        )


def get_shape() -> Shape:
    """
    This function should return any instance of a Shape class
    In our example it is Rectangle or Circle.
    """
    options: list[Shape] = [Rectangle(), Circle(), Square(), Spruce()]
    return choice(options)


def main():
    """
    In Rectangle is used I'd like to see:

    ----
    |  |
    ----

    If Circle is used:
      --
     -  -
      --
    """
    shape: Shape = get_shape()
    shape.draw()


if __name__ == "__main__":
    main()
