import re
from collections import defaultdict

with open("input.txt") as f:
    commands = list(map(lambda x: x.strip("\n"), f.readlines()))

TOTAL_SPACE = 70000000
NEEDED_SPACE = 30000000


def cwd_to_string(cwd):
    return cwd[0] + "/".join(cwd[1:])


def parse_fs(commands):
    cwd = []
    fs = defaultdict(int)
    for command in commands:
        if command.startswith("$ cd"):
            move_cmd = command.split()[-1]
            if move_cmd == "..":
                cwd.pop()
            else:
                cwd.append(move_cmd)
        elif re.match(r"^[0-9]+ ", command):
            size = int(command.split()[0])
            copied_cwd = cwd[:]
            while len(copied_cwd) > 0:
                fs[cwd_to_string(copied_cwd)] += size
                copied_cwd.pop()

    return fs


def solve(fs, threshold, filtering_func, part2=False):
    qualyfing_sizes = []
    for v in fs.values():
        if part2 and v > threshold:
            qualyfing_sizes.append(v)
        elif not part2 and v < threshold:
            qualyfing_sizes.append(v)
    return filtering_func(qualyfing_sizes)


fs = parse_fs(commands)
print("Part 1:", solve(fs, 100000, sum))
print("Part 2:", solve(fs, NEEDED_SPACE - (TOTAL_SPACE - fs["/"]), min, part2=True))
