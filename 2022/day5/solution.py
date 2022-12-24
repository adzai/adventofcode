from collections import defaultdict

with open("input.txt") as f:
    configuration, steps = f.read().split("\n\n")
    configuration = configuration.split("\n")[:-1]
    steps = steps.split("\n")[:-1]

config_map = defaultdict(list)
for line in configuration:
    i = 0
    while i < len(line):
        char = line[i + 1].strip()
        position = i // 4 + 1
        if char != "":
            config_map[position] = [char] + config_map[position]
        i += 4

for step in steps:
    step = step.split()
    num = int(step[1])
    from_step = int(step[3])
    to_step = int(step[5])
    popped_vals = []
    for i in range(num):
        popped_vals.append(config_map[from_step].pop())
        # config_map[to_step].append(config_map[from_step].pop())
    config_map[to_step] += popped_vals[::-1]

top_letters = ""
for key in sorted(config_map.keys()):
    top_letters += config_map[key][-1]

print(top_letters)
