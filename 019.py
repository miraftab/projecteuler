# https://projecteuler.net/problem=19: Counting Sundays
from datetime import date

sundays = 0
for year in range(1901, 2001):
    for month in range(1, 13):
        if date(year=year, month=month, day=1).weekday() == 6:
            sundays += 1

print(sundays)