# https://projecteuler.net/problem=21
import math
from functools import lru_cache

# calculate sum of divisors for n
@lru_cache(None)
def sum_div(n):
    total = 1
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            total += i
            y = n // i
            if y > i:
                total += y
    return total


# calculate sum of amicable numbers bellow limit
def amicable(limit):
    for a in range(limit):
        b = sum_div(a)
        if a != b and sum_div(b) == a:
            yield a


def main():
    print(sum(amicable(10000)))


if __name__ == "__main__":
    main()
