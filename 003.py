# https://projecteuler.net/problem=3

n = 600851475143
i = 2
b = 0
while i <= n / i:
    if n % i == 0:
        n //= i
        b = max(b, i)
    else:
        i += 1
if b < n:
    b = n

print(b)
