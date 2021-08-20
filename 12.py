from math import sqrt


def divisors(n):
    b = []
    j = 1
    while j < sqrt(n) + 1:
        if n % j == 0:
            if j**2 != n:
                b.append(j)
                b.append(int(n / j))
            else:
                b.append(j)
        j += 1
    b.sort(reverse=False)
    return b


def main():
    i = 5
    while len(divisors(int((i*(i+1))/2))) <= 500:
        i += 1
    print(int((i*(i+1))/2))
    print(len(divisors(int((i*(i+1))/2))))


if __name__ == "__main__":
    main()
