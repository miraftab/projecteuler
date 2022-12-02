# https://projecteuler.net/problem=24: Lexicographic permutations
from itertools import permutations
s = list(permutations(range(10)))[999999]
print(''.join(map(str, s)))
