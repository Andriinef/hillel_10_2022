from threading import Thread
from time import sleep


def get_primes(start: int, end: int) -> list[int]:
    results = []
    for number in range(start, end + 1):
        prime = True
        for i in range(2, number):
            if number % i == 0:
                prime = False
                break
        if END > number:
            if prime:
                results.append(number)
    return results


def foo(start: int, end: int):
    sleep(1)
    data = get_primes(start, end)
    print(f"Thread {item+1}: {data}")


if __name__ == "__main__":
    start = 100
    END = 10000
    thread_ = 5
    range_ = int(END / thread_)
    end = range_
    for item in range(thread_):
        if END > start:
            thread = Thread(target=foo, args=[start, end])
            thread.start()
            start = end + 1
            end += range_
            thread.join()
