# https://projecteuler.net/problem=10: Problem 10: Summation of primes
marked = [0] * 2_000_000
value = 3
s = 2
while value < 2_000_000:
    if marked[value] == 0:
        s += value
        i = value
        while i < 2_000_000:
            marked[i] = 1
            i += value
    value += 2
print(s)
