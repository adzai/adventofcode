with open("aoc12-input.txt") as f:
    lines = f.readlines()

# lines = ["F10",
# "N3",
# "F7",
# "R90",
# "F11"]

def part1(lines):
    directions = ["E", "N", "W", "S"]
    sums = [0, 0, 0, 0]
    current_direction = [directions[0], 0]
    for line in lines:
        direction = line[0]
        num = int(line[1:])
        if direction in "LR":
            mod = 1 if direction == "L" else - 1
            index = current_direction[1] + mod
            while num > 0:
                num -= 90
                current_direction[0] = directions[index % 4]
                current_direction[1] = index % 4
                index += mod
        elif direction in directions:
            for i, d in enumerate(directions):
                if d == direction:
                    sums[i] += num
        else:
            sums[current_direction[1]] += num
    return sums

def part2(lines):
    # EAST = +
    # NORTH = +
    waypoint = {"H": 10, "V": 1}
    ship = {"H": 0, "V": 0}
    for line in lines:
        direction = line[0]
        num = int(line[1:])
        if direction in "LR":
            while num > 0:
                if direction == "R":
                    tmp = waypoint["V"]
                    waypoint["V"] = - waypoint["H"]
                    waypoint["H"] = tmp
                else:
                    tmp = waypoint["V"]
                    waypoint["V"] = waypoint["H"]
                    waypoint["H"] = - tmp
                num -= 90
        elif direction in "NESW":
            if direction == "N":
                waypoint["V"] += num
            elif direction == "S":
                waypoint["V"] -= num
            elif direction == "E":
                waypoint["H"] += num
            elif direction == "W":
                waypoint["H"] -= num
        else:
            ship["H"] += num * waypoint["H"]
            ship["V"] += num * waypoint["V"]
    return ship

sums = part1(lines)
print(abs(sums[0] - sums[2]) + abs(sums[1] - sums[3]))
x = part2(lines)
print(sum(list(map(abs, x.values()))))
