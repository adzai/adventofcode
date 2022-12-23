with open("input.txt") as f:
    lines = f.read().split("\n")[:-1]


# lines = ["2-4,6-8", "2-3,4-5", "5-7,7-9", "2-8,3-7", "6-6,4-6", "2-6,4-8"]


def get_pairs(lines):
    pairs = []

    for line in lines:
        first, second = line.split(",")
        first_list = list(map(int, first.split("-")))
        second_list = list(map(int, second.split("-")))
        first_range = range(first_list[0], first_list[1] + 1)
        second_range = range(second_list[0], second_list[1] + 1)
        pairs.append((first_range, second_range))

    return pairs


def contains(l1, l2):
    for x in l2:
        if x not in l1:
            return False

    return True


def overlaps(l1, l2):
    for x in l2:
        if x in l1:
            return True

    return False


def part1(lines):
    return sum(map(lambda pair: contains(pair[0], pair[1]) or contains(pair[1], pair[0]), get_pairs(lines)))


def part2(lines):
    return sum(map(lambda pair: overlaps(pair[0], pair[1]) or overlaps(pair[1], pair[0]), get_pairs(lines)))


print("Part 1:", part1(lines))
print("Part 2:", part2(lines))
