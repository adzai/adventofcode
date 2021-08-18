with open("16.txt") as f:
    lines = f.readlines()


d = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}


def get_sue_number(part2=False):
    final = []
    for line in lines:
        lst = list(map(lambda x: x.strip(), ":".join(line.split(":")[1:]).split(",")))
        cnt = 0
        for l in lst:
            x, y = l.split(":")
            if part2 and (x == "cats" or x == "trees"):
                if d[x] < int(y):
                    cnt += 1
            elif part2 and (x == "pomeranians" or x == "goldfish"):
                if d[x] > int(y):
                    cnt += 1
            else:
                if d[x] == int(y):
                    cnt += 1
        final.append(cnt)
    sue_number = -1
    max_num = -1
    for i, f in enumerate(final):
        if f > max_num:
            max_num = f
            sue_number = i + 1
    return sue_number


print("Part 1: ", get_sue_number())
print("Part 2: ", get_sue_number(part2=True))
