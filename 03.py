# Even Fibonacci numbers

n = 600851475143
i = 2
b = []
while i <= n / i:
    if n % i == 0:
        n /= i
        b.append(i)
    else:
        i += 1
if max(b) < n:
    b.append(n)
print(int(max(b)))
print(set(b))
