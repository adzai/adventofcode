from collections import Counter

with open("aoc6-input.txt") as f:
    lines = f.read().split("\n\n")

cnt_part1 = 0
cnt_part2 = 0
for line in lines:
    line = line.strip()
    line_part1 = line.replace("\n", "")
    set_line_len = len(set(line_part1))
    cnt_part1 += set_line_len
    line_part2 = line.split("\n")
    common_dict = Counter(set(line_part1))
    for ans in line_part2:
        dict2 = Counter(ans)
        common_dict = common_dict & dict2
    cnt_part2 += len(list(common_dict.elements()))

print(cnt_part1)
print(cnt_part2)
