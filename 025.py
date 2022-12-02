# https://projecteuler.net/problem=25: 1000-digit Fibonacci number
from functools import lru_cache


@lru_cache
def fib(n):
    if n < 2:
        return 1
    return fib(n - 1) + fib(n - 2)


def main():
    len_f = 0
    i = 0
    while len_f < 1000:
        len_f = len(str(fib(i)))
        i += 1

    print(i)


if __name__ == "__main__":
    main()
