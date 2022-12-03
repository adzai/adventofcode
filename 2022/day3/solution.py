with open("input.txt") as f:
    lines = list(map(lambda x: x.strip("\n"), f.readlines()))

priority_lookup = {}
for letter in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
    ascii_repr = ord(letter)
    if ascii_repr >= 97:
        ascii_repr -= 96
    else:
        ascii_repr -= 38
    priority_lookup[letter] = ascii_repr


def part1(lines):
    total_prio = 0
    for line in lines:
        first_part = line[: len(line) // 2]
        second_part = line[len(line) // 2:]
        shared_letter = list(set(first_part).intersection(second_part))[0]
        total_prio += priority_lookup[shared_letter]

    return total_prio


def part2(lines):
    idx = 0
    total_prio = 0
    while len(lines) >= idx + 3:
        line1 = lines[idx]
        line2 = lines[idx + 1]
        line3 = lines[idx + 2]
        shared_letter = list(set(line1).intersection(line2, line3))[0]
        total_prio += priority_lookup[shared_letter]
        idx += 3

    return total_prio


print("Part 1:", part1(lines))
print("Part 2:", part2(lines))
