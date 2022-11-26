# https://projecteuler.net/problem=9
# a^2 + b^2 = c^2
# s = a + b + c  = 1000
# -------------
# c = 1 / 2 (s-a + (a^2 / s-a))
# b = s - a - c


def sum_of_sides(s):
    # ans will be list of tuple with 3 member (a, b, c) and a < b < c
    for a in range(1, s // 3):
        # assign 's - a + (a**2 // (s-a))' to c_temp to avoid calculate it twice
        c_temp = s - a + (a**2 // (s - a))
        if (a * a) % (s - a) == 0 and c_temp % 2 == 0:
            c = c_temp // 2
            b = s - a - c
            return a, b, c


a, b, c = sum_of_sides(1000)
print(a * b * c)
