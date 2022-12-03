from threading import Thread
from time import sleep


def get_primes(start: int, end: int, thread: int) -> list[int]:
    _range = int(end / thread)
    _start = start
    _end = _range + start
    results = []

    def inner(results, _start: int, _end: int, item: int):
        _results = []
        for number in range(_start, _end + 1):
            prime = True
            for i in range(2, number):
                if number % i == 0:
                    prime = False
                    break
            if end > number:
                if prime:
                    _results.append(number)
        print(f"Thread {item+1}: {_results}")
        results.extend(_results)

    for item in range(thread):
        if end > _start:
            _thread = Thread(target=inner, args=[results, _start, _end, item])
            _thread.start()
            sleep(1)
            _start = _end + 1
            _end += _range
            _thread.join()
    return results


if __name__ == "__main__":
    thread = 5
    data = get_primes(10, 20, thread)
    print(data)
