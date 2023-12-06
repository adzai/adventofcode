def parse_part1(input):
    times = [int(x) for x in input[0].replace("Time:", "").split(" ") if x != ""]
    distances = [int(x) for x in input[1].replace("Distance:", "").split(" ") if x != ""]

    return times, distances


def parse_part2(input):
    time = int("".join([x for x in input[0].replace("Time:", "").split(" ") if x != ""]))
    distance = int("".join([x for x in input[1].replace("Distance:", "").split(" ") if x != ""]))

    return [time], [distance]


def solve(times, distances):
    ways = []
    for time, distance in zip(times, distances):
        min = 0
        for i in range(1, time - 1):
            if i * (time - i) > distance:
                min = i
                break
        max = 0
        for i in range(time - 1, 1, -1):
            if i * (time - i) > distance:
                max = i
                break

        ways.append(max - min + 1)

    total_ways = 1
    for way in ways:
        total_ways *= way

    return total_ways


if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read().split("\n")[:-1]

    times_part1, distances_part1 = parse_part1(input)
    print("Part 1:", solve(times_part1, distances_part1))

    times_part2, distances_part2 = parse_part2(input)
    print("Part 2:", solve(times_part2, distances_part2))
