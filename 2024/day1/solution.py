from collections import defaultdict

if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read().split("\n")[:-1]

    left_list, right_list = [], []
    right_dict = defaultdict(int)
    for row in input:
        left, right = row.split()
        left_list.append(int(left))
        right_list.append(int(right))
        right_dict[int(right)] += 1

    part1_distance, part2_distance = 0, 0
    for left, right in zip(sorted(left_list), sorted(right_list)):
        part1_distance += abs(left - right)
        part2_distance += right_dict[left] * left


    print("Part 1:", part1_distance)
    print("Part 2:", part2_distance)
