import re

with open("inputs/day04.txt") as f:
    partOne = 0
    partTwo = 0
    for line in f.read().split("\n"):
        a, b, c, d = [int(x) for x in re.split("[,-]", line)]
        e1 = set(range(a, (b + 1)))
        e2 = set(range(c, (d + 1)))
        if (a <= c and b >= d) or (c <= a and d >= b):
            partOne += 1
        if e1.intersection(e2):
            partTwo += 1  # 859
print(partOne)
print(partTwo)
