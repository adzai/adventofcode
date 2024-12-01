from typing import Counter


def solve(input, part2):
    matrix = [[]] * len(input[0])
    for row in input:
        for j, col in enumerate(row):
            matrix[j] = matrix[j] + [col]

    return "".join([Counter(col).most_common()[-1 if part2 else 0][0][0] for col in matrix])


if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read().split("\n")[:-1]

    print("Part 1:", solve(input, part2=False))
    print("Part 2:", solve(input, part2=True))
