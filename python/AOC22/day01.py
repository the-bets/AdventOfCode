def main():
    with open("inputs/day01.txt") as f:
        elves = sorted(sum([int(x) for x in y.split("\n")])
                       for y in f.read().split("\n\n"))
        print("Part 1: ", elves[-1])
        print("Part 2: ", sum(elves[-3:]))


if __name__ == "__main__":
    main()
