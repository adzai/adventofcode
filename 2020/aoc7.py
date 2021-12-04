import re

def prepare_input():
    with open("aoc7-input.txt") as f:
        lines = f.readlines()
    LINE_RE = re.compile(r"[0-9]?\s?\w+\s\w+(?=\sbags?)")
    test = re.findall(LINE_RE, str(lines))
    return [re.findall(LINE_RE, line) for line in lines]

def find_colors(check_color, part1=True):
    num_of_bags = 0
    for line in lines:
        color = line[0]
        bags = line[1:]
        if part1:
            if check_color in " ".join(bags) and color not in colors:
                colors.append(color)
                find_colors(color)
        else:
            if check_color == color:
                for bag in bags:
                    bag = bag.split()
                    try:
                        num = int(bag[0])
                        bag_color = bag[1] + " " + bag[2]
                        num_of_bags += num + num * \
                                       find_colors(bag_color, part1=False)
                    except:
                        pass
    return num_of_bags

colors = []
lines = prepare_input()
find_colors("shiny gold")
print("Part 1:", len(colors))
print("Part 2:", find_colors("shiny gold", part1=False))
