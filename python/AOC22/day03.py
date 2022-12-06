import string


def priorityPartOne(a: set, b: set) -> int:
    prio = 0
    prio += int(string.ascii_letters.index(
        "".join(set(a).intersection(b)))) + 1
    return prio


def one(l: list) -> int:
    prio = 0
    for i in l:
        b, c = i[:len(i) // 2], i[len(i) // 2:]
        prio += priorityPartOne(b, c)
    return prio


def two(l: list) -> int:
    prio = 0
    for i in range(len(l) // 3):
        match = set(string.ascii_letters)
        for item in l[i*3:i*3+3]:
            match = match.intersection(set(item))
        prio += string.ascii_letters.index(next(iter(match))) + 1
    return prio


with open("inputs/day03.txt") as f:
    l = f.read().splitlines()
one = one(l)
two = two(l)
print(f"Part One: {one}, Part Two: {two}")
