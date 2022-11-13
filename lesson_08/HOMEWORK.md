# HOMEWORK_08

- Comlete this piece of a code
- Заполните этот фрагмент кода

```python
from abc import ABC, abstractclassmethod
from random import choice


class Shape(ABC):
    @abstractclassmethod
    def draw(self):
        pass


class Rectangle(Shape):
    """Change me. Измени меня."""


class Circle(Shape):
    """Change me. Измени меня."""


def get_shape() -> Shape:
    """
    This function should return any instance of a Shape class
    In our example it is Rectangle or Circle.
    Эта функция должна возвращать любой экземпляр класса Shape.
     В нашем примере это прямоугольник или круг.
    """
    options: list[Shape] = [change_me]
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
```
