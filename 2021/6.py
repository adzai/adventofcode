from collections import Counter

with open("6.input") as f:
    sequence = list(map(int, f.read().split(",")))


def solve(iterations):
    fish_count_lst = [0] * 9
    for k, v in Counter(sequence).items():
        fish_count_lst[k] = v
    for _ in range(iterations):
        num_of_fish = fish_count_lst.pop(0)
        fish_count_lst[6] += num_of_fish
        fish_count_lst.append(num_of_fish)
    return sum(fish_count_lst)


print("Part 1:", solve(80))
print("Part 2:", solve(256))
