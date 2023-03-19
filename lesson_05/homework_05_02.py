""" Создать свою версию такого класса,
    который бы поддерживал интерфейс стандартного range,
    но работал при этом с float.
"""


class frange:
    def __init__(self, start_or_stop, stop=None, step=1.0):
        if stop is None:
            start, stop = 0.0, start_or_stop
        else:
            start, stop = start_or_stop, stop
        self.start, self.stop, self.step = start, stop, step
        self.current = self.start

    def __iter__(self):
        return self

    def __next__(self):
        if self.step > 0 and self.current >= self.stop:
            raise StopIteration
        elif self.step < 0 and self.current <= self.stop:
            raise StopIteration
        result = self.current
        self.current += self.step
        return result


for i in frange(1, 10, 3.5):
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
