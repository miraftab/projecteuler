# Problem 22: Names scores
import csv


with open("p022_names.txt") as f:
    reader = csv.reader(f)
    names = list(reader)
    names[0].sort()
    sum_name = 0
    i = 1
    for name in names[0]:
        s = 0
        for c in name.replace(" ", ""):
            s += ord(c) % 32
        sum_name += s * i
        i += 1
print(sum_name)
