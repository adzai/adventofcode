lines = []
with open("19.txt") as f:
    lines = list(map(lambda x: x.strip().split(), f.readlines()))

# lines = [
# "e => H",
# "e => O",
# "H => HO",
# "H => OH",
# "O => HH",
# "",
# ["HOHOHO"]]

sequence = lines[-1][0]

table = dict()
for line in lines[:-2]:
    key = line[0]
    val = line[-1]
    if table.get(key):
        table[key] += [val]
    else:
        table[key] = [val]


def part1(sequence, table):
    double_char = ""
    result_table = dict()
    for i, char in enumerate(sequence):
        if i > 0:
            double_char = sequence[i - 1] + sequence[i]
        if table.get(char):
            for val in table[char]:
                result_table[sequence[:i] + val + sequence[i + 1 :]] = None
        if table.get(double_char):
            for val in table[double_char]:
                result_table[sequence[: i - 1] + val + sequence[i + 1 :]] = None
    return len(result_table.keys())


def part2(sequence, table):
    new_table = dict()
    for k, v in table.items():
        for val in v:
            length = len(val)
            if new_table.get(length):
                new_table[length] += [{k: val}]
            else:
                new_table[length] = [{k: val}]
    steps = 0
    while sequence != "e":
        for i in reversed(sorted(new_table.keys())):
            for d in new_table[i]:
                for k in sorted(d.keys()):
                    while sequence.find(d[k]) != -1:
                        sequence = sequence.replace(
                            d[k], k, 1
                        )  # replace only 1, not multiple ...
                        steps += 1
                        if sequence == "e":
                            return steps
    return steps


print("Part 1:", part1(sequence, table))
print("Part 2:", part2(sequence, table))
