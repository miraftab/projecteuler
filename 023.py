# https://projecteuler.net/problem=23: Non-abundant sums
# Brute Force Solution must be optimized - it is very long!
abundant_nums = []


def abundant():
    global abundant_nums
    for i in range(11, 28123):
        divisor_sum = 0
        for j in range(1, (i // 2 + 1)):
            if i % j == 0:
                divisor_sum += j
        if divisor_sum > i:
            abundant_nums.append(i)

def sum_non_abundant():
    global abundant_nums
    result = 0
    for i in range(1, 28123):
        for a in abundant_nums:
            diff = i - a
            if diff in abundant_nums:
                break
        else:
            result += i
            print(i)
    return result

def main():
    abundant()
    print('1st phase done!')
    print(sum_non_abundant())


if __name__ == "__main__":
    main()
