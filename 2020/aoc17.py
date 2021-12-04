with open("aoc17-input.txt") as f:
    lines = f.readlines()

# lines = [".#.", # "..#", # "###"]
# print(grid[0][1][2])


def find_active(grid):
    coordinates = []
    for z in grid.keys():
        for y in range(len(grid[z])):
            for x in range(len(grid[z][y])):
                if grid[z][y][x] == "#":
                    coordinates.append((x, y, z))
    return coordinates

# print(find_active(grid))
def is_neighbor(first, second):
    for num1, num2 in zip(first, second):
        if abs(num1 - num2) > 1:
            return False
    return True

def add_new(coordinates, bounds):
    to_add = []
    lowest_z, highest_z = bounds[2][0] - 1, bounds[2][1] + 1
    lowest_y, highest_y = -1, bounds[1][1] + 1
    lowest_x, highest_x = -1, bounds[0][1] + 1
    for z in range(lowest_z, highest_z + 1):
        for y in range(lowest_y, highest_y + 1):
            for x in range(lowest_x, highest_x + 1):
                current_neighbors = 0
                for active in coordinates:
                    if is_neighbor(active, (x, y, z)):
                        current_neighbors += 1
                if current_neighbors == 3:
                    to_add.append((x, y, z))
    return to_add

def adjust_active(coordinates):
    to_remove = []
    for active in coordinates:
        neighbors = 0
        for i in range(len(coordinates)):
            if active != coordinates[i]:
                if is_neighbor(active, coordinates[i]):
                    neighbors += 1
        if not (neighbors == 2 or neighbors == 3):
            to_remove.append(active)
    for c in to_remove:
        coordinates.remove(c)
    return coordinates

def find_extremities(to_activate):
    smallest_z, highest_z, smallest_x, highest_x, smallest_y, \
    highest_y = 10000, -10000, 10000, -10000, 10000, -10000
    for nums in to_activate:
        if nums[0] < smallest_x:
            smallest_x = nums[0]
        elif nums[0] > highest_x:
            highest_x = nums[0]
        if nums[1] < smallest_y:
            smallest_y = nums[1]
        elif nums[1] > highest_y:
            highest_y = nums[1]
        if nums[2] < smallest_z:
            smallest_z = nums[2]
        elif nums[2] > highest_z:
            highest_z = nums[2]
    shift_x = 0
    while smallest_x < 0:
        shift_x += 1
        smallest_x += 1
    highest_x += shift_x
    shift_y = 0
    while smallest_y < 0:
        shift_y += 1
        smallest_y += 1
    highest_y += shift_y
    return ((shift_x, highest_x), (shift_y, highest_y),
        (smallest_z, highest_z))

def print_cycle(to_activate, bounds, grid):
    shift_x = bounds[0][0]
    shift_y = bounds[1][0]
    for z in range(bounds[2][0], bounds[2][1] + 1):
        cols = []
        for y in range(bounds[1][1] + 1):
            row = []
            for x in range(bounds[0][1] + 1):
                row.append(".")
            cols.append(row)
        grid[z] = cols
    for active in to_activate:
        y = active[1] + shift_y
        x = active[0] + shift_x
        grid[active[2]][y][x] = "#"
    return grid

def solve1(lines):
    grid = {0: lines}
    bounds = ((-1, len(grid[0])), (-1, len(grid[0])), (-1, 1))
    for i in range(6):
        coordinates = find_active(grid)
        to_add = add_new(coordinates, bounds)
        to_activate = adjust_active(coordinates) + to_add
        bounds = find_extremities(to_activate)
        grid = print_cycle(to_activate, bounds, grid)
    return len(find_active(grid))

print("Part 1:", solve1(lines))

def find_active2(grid):
    coordinates = []
    for w in grid.keys():
        for z in grid[w].keys():
            for y in range(len(grid[w][z])):
                for x in range(len(grid[w][z][y])):
                    if grid[w][z][y][x] == "#":
                        coordinates.append((x, y, z, w))
    return coordinates

def add_new2(coordinates, bounds):
    to_add = []
    lowest_w, highest_w = bounds[3][0] - 1, bounds[3][1] + 1
    lowest_z, highest_z = bounds[2][0] - 1, bounds[2][1] + 1
    lowest_y, highest_y = -1, bounds[1][1] + 1
    lowest_x, highest_x = -1, bounds[0][1] + 1
    for w in range(lowest_w, highest_w + 1):
        for z in range(lowest_z, highest_z + 1):
            for y in range(lowest_y, highest_y + 1):
                for x in range(lowest_x, highest_x + 1):
                    current_neighbors = 0
                    for active in coordinates:
                        if is_neighbor(active, (x, y, z, w)):
                            current_neighbors += 1
                    if current_neighbors == 3:
                        to_add.append((x, y, z, w))
    return to_add

def find_extremities2(to_activate):
    smallest_w, highest_w, smallest_z, highest_z, smallest_x, highest_x, smallest_y, \
    highest_y = 10000, -10000, 10000, -10000, 10000, -10000, 10000, -10000
    for nums in to_activate:
        if nums[0] < smallest_x:
            smallest_x = nums[0]
        elif nums[0] > highest_x:
            highest_x = nums[0]
        if nums[1] < smallest_y:
            smallest_y = nums[1]
        elif nums[1] > highest_y:
            highest_y = nums[1]
        if nums[2] < smallest_z:
            smallest_z = nums[2]
        elif nums[2] > highest_z:
            highest_z = nums[2]
        if nums[3] < smallest_w:
            smallest_w = nums[3]
        elif nums[3] > highest_w:
            highest_w = nums[3]
    shift_x = 0
    while smallest_x < 0:
        shift_x += 1
        smallest_x += 1
    highest_x += shift_x
    shift_y = 0
    while smallest_y < 0:
        shift_y += 1
        smallest_y += 1
    highest_y += shift_y
    return ((shift_x, highest_x), (shift_y, highest_y),
        (smallest_z, highest_z), (smallest_w, highest_z))

def print_cycle2(to_activate, bounds, grid):
    shift_x = bounds[0][0]
    shift_y = bounds[1][0]
    for w in range(bounds[3][0], bounds[3][1] + 1):
        z_dict = dict()
        for z in range(bounds[2][0], bounds[2][1] + 1):
            cols = []
            for y in range(bounds[1][1] + 1):
                row = []
                for x in range(bounds[0][1] + 1):
                    row.append(".")
                cols.append(row)
            z_dict[z] = cols
        grid[w] = z_dict.copy()
    for active in to_activate:
        y = active[1] + shift_y
        x = active[0] + shift_x
        grid[active[3]][active[2]][y][x] = "#"
    return grid

def solve2(lines):
    grid = {0: {0: lines}}
    bounds = ((0, 7), (0, 7), (0, 0), (0, 0))
    for i in range(6):
        coordinates = find_active2(grid)
        to_add = add_new2(coordinates, bounds)
        to_activate = adjust_active(coordinates) + to_add
        bounds = find_extremities2(to_activate)
        grid = print_cycle2(to_activate, bounds, grid)

    return len(find_active2(grid))

print("Part 2:", solve2(lines))
