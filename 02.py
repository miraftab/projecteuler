# Even Fibonacci numbers

a, b = 1, 2
sum_f = 0
while b < 4000000:
    if b % 2 == 0:
        sum_f += b
    a, b = b, a + b
print(sum_f)
