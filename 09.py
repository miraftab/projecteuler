# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
from functools import reduce


def pythagoras2(num):
    for a in range(1, int(num / 3) + 1):
        if (a * a) % (num - a) == 0:
            c = int((num - a + (a * a / (num - a))) / 2)
            b = int(num - a-c)
            if a ** 2 + b ** 2 == c ** 2:
                return a, b, c
    return 'Impossible'


print(reduce(lambda x, y: x * y, pythagoras2(1000)))
