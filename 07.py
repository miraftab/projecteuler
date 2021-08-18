# What is the 10 001st prime number?
from math import sqrt


def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    elif n % 3 == 0:
        return False
    elif n < 9:
        return True
    else:
        for i in range(5, int(sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
    return True


primes = []
j = 2
while len(primes) < 10001:
    if is_prime(j):
        primes.append(j)
    j += 1

print(primes[-1])
