import json

with open("11-input.txt") as f:
    d = json.load(f)


def loop_dict(d, part2=False):
    sum = 0
    for v in d.values():
        if part2 and v == "red":
            return 0
        elif isinstance(v, dict):
            sum += loop_dict(v, part2=part2)
        elif isinstance(v, list):
            sum += sum_list(v, part2=part2)
        elif isinstance(v, int):
            sum += v
    return sum


def sum_list(lst, part2=False):
    sum = 0
    for val in lst:
        if isinstance(val, int):
            sum += val
        elif isinstance(val, dict):
            sum += loop_dict(val, part2=part2)
        elif isinstance(val, list):
            sum += sum_list(val, part2=part2)
    return sum


print("Part 1: ", loop_dict(d))
print("Part 2: ", loop_dict(d, part2=True))
