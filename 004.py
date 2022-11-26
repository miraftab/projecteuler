# https://projecteuler.net/problem=4

b = []
for i in range(100, 1000):
    for j in range(100, 1000):
        s = i * j
        if s == int(str(s)[::-1]):
            b.append(s)
print(max(b))
