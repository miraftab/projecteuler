# https://projecteuler.net/problem=27: Quadratic primes
import math

primes = []


def is_prime(n):
    if n in primes:
        return True
    elif n < 1000:
        return False
    else:
        if n % 2 == 0:
            return False
        for i in range(3, int(math.sqrt(n) + 1), 2):
            if n % i == 0:
                return False
        return True


def primes_below_1000():
    for i in range(2, 1000):
        for p in primes:
            if i % p == 0:
                break
        else:
            primes.append(i)


def main():
    primes_below_1000()
    max_len = 0
    for b in primes:
        for a in range(-1000, 1000):
            n = 0
            l = 0
            while is_prime(n**2 + a * n + b):
                l += 1
                n += 1
            if l > max_len:
                max_len = l
                axb = a * b
    print(axb)



if __name__ == "__main__":
    main()
