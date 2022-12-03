def get_primes(start: int, end: int) -> list[int]:
    results = []
    for number in range(start, end + 1):
        prime = True
        for i in range(2, number):
            if number % i == 0:
                prime = False
                break
        if prime:
            results.append(number)
    return results


data = get_primes(1, 100)
print(data)
