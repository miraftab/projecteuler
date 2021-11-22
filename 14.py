count = 0
collatz = (1, 1)
for i in range(13, 1000000):
    n = i
    while n != 1:
        if n % 2 == 0:
            n = int(n / 2)
        else:
            n = 3 * n + 1
        count += 1
    if count > collatz[1]:
        collatz = (i, count)
        print(collatz)
    count = 0
print(collatz)
