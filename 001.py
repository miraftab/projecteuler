# https://projecteuler.net/problem=1
# print(sum(i for i in range(1000) if (i % 3 == 0) or (i % 5 == 0)))
def main():
    s = 0
    for i in range(1000):
        s += i if (i % 3 == 0) or (i % 5 == 0) else 0
    print(s)


if __name__ == '__main__':
    main()