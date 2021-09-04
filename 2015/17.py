import itertools


def day17():
    with open("17.txt") as f:
        lines = f.readlines()
    nums = [int(num) for num in lines]
    combinations_list = []
    minimum = len(nums)
    for i in range(len(nums)):
        for combination in itertools.combinations(nums, i):
            if sum(combination) == 150:
                combinations_list.append(combination)
                minimum = min(len(combination), minimum)
    min_combs = [comb for comb in combinations_list if len(comb) == minimum]
    return len(combinations_list), len(min_combs)


part1, part2 = day17()
print("Part 1:", part1)
print("Part 2:", part2)
