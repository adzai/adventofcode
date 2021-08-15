import itertools
import re


def get_score(flavors, nums):
    capacity = max(sum([x["capacity"] * y for x, y in zip(flavors, nums)]), 0)
    durability = max(sum([x["durability"] * y for x, y in zip(flavors, nums)]), 0)
    flavor = max(sum([x["flavor"] * y for x, y in zip(flavors, nums)]), 0)
    texture = max(sum([x["texture"] * y for x, y in zip(flavors, nums)]), 0)
    calories = sum([x["calories"] * y for x, y in zip(flavors, nums)])
    return capacity * durability * flavor * texture, calories


def gen_valid_sums(n, r1, r2):
    ranges = (range(r1, r2) for _ in range(n))
    numbers = itertools.product(*ranges)
    return [x for x in numbers if sum(x) == 100]


def gen_valid_sums_hardcoded():
    sums = []
    for i in range(1, 100):
        for j in range(1, 100 - i):
            for k in range(1, 100 - i - j):
                l = 100 - i - j - k
                sums.append([i, j, k, l])
    return sums


def day15():
    with open("15.txt") as f:
        lines = f.readlines()
    flavors = []
    for line in lines:
        capacity, durability, flavor, texture, calories = list(
            map(int, re.findall(r"-?\d+", line))
        )
        flavors.append(
            {
                "capacity": capacity,
                "durability": durability,
                "flavor": flavor,
                "texture": texture,
                "calories": calories,
            }
        )
    max_score_part1 = 0
    max_score_part2 = 0
    # sums = gen_valid_sums(4, 1, 97)
    sums = gen_valid_sums_hardcoded()
    for s in sums:
        current_score, calories = get_score(flavors, s)
        max_score_part1 = max(max_score_part1, current_score)
        if calories == 500:
            max_score_part2 = max(max_score_part2, current_score)

    print("Part 1:", max_score_part1)
    print("Part 2:", max_score_part2)


day15()
