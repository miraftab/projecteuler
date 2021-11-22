# Smallest multiple

from functools import reduce

n = [1]
for i in range(1, 21):
    num = i
    for item in n:
        if num % item == 0:
            num /= item
    n.append(int(num))
result = reduce(lambda x, y: x * y, n)
print(result)
