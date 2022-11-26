# https://projecteuler.net/problem=6

result1, result2 = 0, 0
for i in range(1, 101):
    result1 += i**2
result2 = (1 + 100) * 100 // 2
result2 = result2**2
print(result2 - result1)
