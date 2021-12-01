with open("1.txt") as f:
    input = list(map(int, f.readlines()))

# input = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]


def part1():
    increases = 0
    for i in range(1, len(input)):
        if input[i] > input[i - 1]:
            increases += 1
    return increases


def part2():
    d = dict()
    increases = 0
    for i, num in enumerate(input):
        if not d.get(i):
            d[i] = [num]
        if i - 1 >= 0:
            d[i - 1].append(num)
        if i - 2 >= 0:
            d[i - 2].append(num)

    print(d)
    for i in range(1, len(d.keys())):
        if sum(d[i]) > sum(d[i - 1]):
            increases += 1
    return increases


print("Part 1:", part1())
print("Part 2:", part2())
