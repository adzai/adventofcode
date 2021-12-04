from collections import defaultdict

with open("aoc24exp.txt") as f:
    lines = f.readlines()

d = defaultdict(int)

for line in lines:
    current = {"se": 0, "sw": 0, "ne": 0, "nw": 0, "e": 0, "w": 0}
    i = 0
    while i < len(line):
        if line[i] == "s":
            if i + 1 < len(line):
                if line[i+1] in "ew":
                    current[line[i] + line[i+1]] -= 1
                i += 2
            else:
                current[line[i]] += 1
                i += 1
        elif line[i] == "n":
            if i + 1 < len(line):
                if line[i+1] in "ew":
                    current[line[i] + line[i+1]] += 1
                i += 2
            else:
                current[line[i]] += 1
                i += 1
        elif line[i] == "e":
            current[line[i]] -= 1
            i += 1
        elif line[i] == "2":
            current[line[i]] += 1
            i += 1
        else:
            i += 1

    tup = (current["ne"] - current["sw"], current["nw"] - current["se"], current["w"] - current["e"])
    d[sum(list(tup))] += 1
print(d)

black = 0
for item in d:
    if d[item] == 1:
        black += 1

print(black)
