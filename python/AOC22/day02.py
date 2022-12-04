partOnePlays = {
    "A Y": 8, "A X": 4, "A Z": 3,
    "B Z": 9, "B Y": 5, "B X": 1,
    "C X": 7, "C Z": 6, "C Y": 2,
}

partTwoPlays = {
    "A Y": 4, "A X": 3, "A Z": 8,
    "B Z": 9, "B Y": 5, "B X": 1,
    "C X": 2, "C Z": 7, "C Y": 6,
}


def main():
    with open("inputs/day02.txt") as f:
        games = f.read().split("\n")
        partOne = sum(partOnePlays[x] for x in games)
        partTwo = sum(partTwoPlays[y] for y in games)
        print(f"Part One is: {partOne}, and Part Two is: {partTwo}")


if __name__ == "__main__":
    main()
