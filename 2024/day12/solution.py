from collections import defaultdict

UP, DOWN, LEFT, RIGHT = (-1, 0), (1, 0), (0, -1), (0, 1)


class Region:
    def __init__(self, letter, x, y, area, perimeter):
        self.letter = letter
        self.area = area
        self.perimeter = perimeter
        self.coordinates = [(x, y)]
        self.sides = 0
        self.counted_sides = [False, False, False, False]

    def __repr__(self) -> str:
        return f"{self.letter} <> area: {self.area}, perimeter: {self.perimeter}, sides: {self.sides}"


def is_in_bounds(x, y, x_bound, y_bound):
    return 0 <= x and x < x_bound and 0 <= y and y < y_bound


def calculate_perimeter(grid, x, y):
    current_letter = grid[x][y]
    x_bound, y_bound = len(grid), len(grid[0])
    perimeter = 0
    for direction_x, direction_y in [UP, DOWN, LEFT, RIGHT]:
        if (
            not is_in_bounds(x + direction_x, y + direction_y, x_bound, y_bound)
            or grid[x + direction_x][y + direction_y] != current_letter
        ):
            perimeter += 1

    return perimeter


def generate_neighbors(grid, x, y, letter):
    neighbors = []
    for dir_x, dir_y in [UP, DOWN, LEFT, RIGHT]:
        if is_in_bounds(dir_x + x, dir_y + y, len(grid), len(grid[0])) and grid[dir_x + x][dir_y + y] == letter:
            neighbors.append((dir_x + x, dir_y + y))

    return neighbors


def get_region(grid, x, y, visited):
    letter = grid[x][y]
    region = Region(letter, x, y, 1, calculate_perimeter(grid, x, y))
    to_visit = generate_neighbors(grid, x, y, letter)
    visited.add((x, y))
    while len(to_visit) > 0:
        coordinates = to_visit.pop(0)
        if coordinates in visited:
            continue

        visited.add(coordinates)

        if (
            is_in_bounds(coordinates[0], coordinates[1], len(grid), len(grid[0]))
            and grid[coordinates[0]][coordinates[1]] == letter
        ):
            region.coordinates.append(coordinates)
            region.area += 1
            region.perimeter += calculate_perimeter(grid, coordinates[0], coordinates[1])
            visited.add(coordinates)
            to_visit.extend(generate_neighbors(grid, coordinates[0], coordinates[1], letter))

    return region


if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read().split("\n")[:-1]

    grid = [list(row) for row in input]
    x_bound, y_bound = len(grid), len(grid[0])

    d = {}
    global_visited = set()
    regions = []
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if (i, j) not in global_visited:
                regions.append(get_region(grid, i, j, global_visited))

    total = 0
    for region in regions:
        total += region.area * region.perimeter

    print("Part 1:", total)
