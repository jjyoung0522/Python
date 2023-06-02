import sys

def sieve_eratosthenes(limit):
    numbers = [True] * (limit + 1)
    numbers[0] = numbers[1] = False
    for p in range(2, int(limit ** 0.5) + 1):
        if numbers[p]:
            for i in range(p * p, limit + 1, p):
                numbers[i] = False
    return numbers

limit = 123456 * 2
primes = sieve_eratosthenes(limit)

a = int(sys.stdin.readline())

while a != 0:
    count = sum(1 for k in range(a + 1, a * 2 + 1) if primes[k])
    print(count)
    a = int(sys.stdin.readline())
