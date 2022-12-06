import string


def findPriority(a: set, b: set) -> int:
    prio = int(string.ascii_letters.index(
        "".join(set(a).intersection(b)))) + 1
    return prio


with open("inputs/day03.txt", "r") as f:
    prio = 0
    for l in f:
        a, b = l[:len(l) // 2], l[len(l) // 2:]
        prio += findPriority(a, b)
    print(f"Part One: Priority is {prio}")
