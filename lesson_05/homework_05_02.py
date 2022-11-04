""" Создать свою версию такого класса,
    который бы поддерживал интерфейс стандартного range,
    но работал при этом с float.
"""


class frange:
    def __init__(self, start, end=None, step=1):
        if end is None:
            self.start = 0
            self.end = start
        else:
            self.start = start
            self.end = end
        self.step = step

    def __iter__(self):
        if self.step > 0:
            while self.start < self.end:
                i = self.start
                yield i
                self.start += self.step
        else:
            while self.start > self.end:
                i = self.start
                yield i
                self.start += self.step

    def __next__(self):
        pass


for i in frange(1, 100, 3.5):
    print(i)


assert list(frange(5)) == [0, 1, 2, 3, 4]
assert list(frange(2, 5)) == [2, 3, 4]
assert list(frange(2, 10, 2)) == [2, 4, 6, 8]
assert list(frange(10, 2, -2)) == [10, 8, 6, 4]
assert list(frange(2, 5.5, 1.5)) == [2, 3.5, 5]
assert list(frange(1, 5)) == [1, 2, 3, 4]
assert list(frange(0, 5)) == [0, 1, 2, 3, 4]
assert list(frange(0, 0)) == []
assert list(frange(100, 0)) == []

print("SUCCESS!")
