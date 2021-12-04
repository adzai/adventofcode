from collections import defaultdict

with open("3.txt") as f:
    string = f.read()

x = 0
y = 0
d = defaultdict(int)

for char in string:
    if char == "^":
        y += 1
    elif char == "<":
        x -= 1
    elif char == ">":
        x += 1
    elif char == "v":
        y -= 1

    d[(x, y)] += 1

print("Part 1:", len(d.keys()))
