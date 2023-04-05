import time

with open("14.txt") as f:
    lines = f.read().split("\n")[:-1]


def cartesian(val1, val2) -> list[tuple[int, int]]:
    if isinstance(val1, list):
        return [(lst_val, val2) for lst_val in val1]
    return [(val1, lst_val) for lst_val in val2]


def smart_range(x, y):
    return list(range(min(x, y), max(x, y) + 1))


def create_lists(val):
    outer = []
    for _ in range(val):
        inner = []
        for _ in range(val):
            inner.append(".")

        outer.append(inner)

    return outer


class Simulation:
    def __init__(self, env_scale, print_offset):
        self.env_scale = env_scale
        self.environment = create_lists(env_scale)
        self.print_offset = print_offset
        self.highest_y = 0

    def parse(self, lines):
        previous_coords = None
        for line in lines:
            for x_y in line.split(" -> "):
                x, y = x_y.split(",")
                x = int(x)
                y = int(y)
                if not previous_coords:
                    previous_coords = (x, y)
                    continue
                if x == previous_coords[0]:
                    coords_to_draw = cartesian(x, smart_range(y, previous_coords[1]))
                elif y == previous_coords[1]:
                    coords_to_draw = cartesian(smart_range(x, previous_coords[0]), y)
                else:
                    raise Exception("X or Y not same as previous step")

                for coords in coords_to_draw:
                    self.environment[coords[1]][coords[0] - self.print_offset] = "#"
                    self.highest_y = max(coords[1], self.highest_y)

                previous_coords = (x, y)

            previous_coords = None

    def print(self):
        for row in self.environment:
            print("".join(row))

    def sim_one_sand_unit(self, part2=False):
        sand_x, sand_y = (500 - self.print_offset, 0)
        while True:
            try:
                if part2 and sand_y - 1 == self.highest_y:
                    self.environment[sand_y][sand_x] = "O"
                    return True
                if self.environment[sand_y + 1][sand_x] not in "#O":
                    sand_y += 1
                elif self.environment[sand_y + 1][sand_x - 1] not in "#O":
                    sand_y += 1
                    sand_x -= 1
                elif self.environment[sand_y + 1][sand_x + 1] not in "#O":
                    sand_y += 1
                    sand_x += 1
                elif self.environment[sand_y][sand_x] == ".":
                    self.environment[sand_y][sand_x] = "O"
                    return True
                else:
                    return False

            except IndexError:
                if part2 and sand_y - 1 != self.highest_y:
                    continue
                return False


def part1(row_size=1000, time_delay=False):
    sim = Simulation(row_size, 494)
    sim.parse(lines)
    num_of_sand_units_that_came_to_rest = 0
    while sim.sim_one_sand_unit():
        if time_delay:
            sim.print()
            time.sleep(time_delay)
        num_of_sand_units_that_came_to_rest += 1

    print(
        f"Part 1: Sand fell into abyss after {num_of_sand_units_that_came_to_rest} units!"
    )


def part2(row_size=5000, time_delay=False):
    sim = Simulation(row_size, 0)
    sim.parse(lines)
    num_of_sand_units_that_came_to_rest = 0
    while sim.sim_one_sand_unit(part2=True):
        if time_delay:
            sim.print()
            time.sleep(time_delay)
        num_of_sand_units_that_came_to_rest += 1

    print(
        f"Part 2: Sand fell into abyss after {num_of_sand_units_that_came_to_rest} units!"
    )


part1()
part2()
