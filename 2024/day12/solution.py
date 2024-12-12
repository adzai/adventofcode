from collections import defaultdict

UP, DOWN, LEFT, RIGHT = (-1, 0), (1, 0), (0, -1), (0, 1)


class Region:
    def __init__(self, letter, x, y, area, perimeter):
        self.letter = letter
        self.area = area
        self.perimeter = perimeter
        self.coordinates = [(x, y)]
        self.sides = 0

    def __repr__(self) -> str:
        return f"{self.letter} <> area: {self.area}, perimeter: {self.perimeter}, sides: {self.sides}"


def calculate_perimeter(grid, x, y):
    current_letter = grid.get((x, y))
    perimeter = 0
    for direction_x, direction_y in [UP, DOWN, LEFT, RIGHT]:
        if (next_letter := grid.get((x + direction_x, y + direction_y))) is None or next_letter != current_letter:
            perimeter += 1

    return perimeter


def get_neighbors(grid, x, y, letter):
    neighbors = []
    for dir_x, dir_y in [UP, DOWN, LEFT, RIGHT]:
        if (next_letter := grid.get((dir_x + x, dir_y + y))) and next_letter == letter:
            neighbors.append((dir_x + x, dir_y + y))

    return neighbors


def get_sides(grid, x, y):
    current_cell = grid.get((x, y))
    res = []
    for pair_one, pair_two in [(UP, LEFT), (UP, RIGHT), (DOWN, LEFT), (DOWN, RIGHT)]:
        up_cell = grid.get((x + pair_one[0], y + pair_one[1]))
        left_cell = grid.get((x + pair_two[0], y + pair_two[1]))
        up_left_cell = grid.get((x + pair_one[0], y + pair_two[1]))
        res.append(
            (up_cell != current_cell and left_cell != current_cell)
            or (left_cell == current_cell and up_cell == current_cell and up_left_cell != current_cell)
        )

    return sum(res)


def get_region(grid, x, y, visited):
    letter = grid.get((x, y))
    region = Region(letter, x, y, 0, 0)
    to_visit = [(x, y)]
    while len(to_visit) > 0:
        coordinates = to_visit.pop(0)
        if coordinates in visited:
            continue

        visited.add(coordinates)

        if (next_letter := grid.get((coordinates[0], coordinates[1]))) is not None and next_letter == letter:
            region.coordinates.append(coordinates)
            region.area += 1
            region.perimeter += calculate_perimeter(grid, coordinates[0], coordinates[1])
            region.sides += get_sides(grid, coordinates[0], coordinates[1])
            visited.add(coordinates)
            to_visit.extend(get_neighbors(grid, coordinates[0], coordinates[1], letter))

    return region


if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read().split("\n")[:-1]

    grid = {(x, y): cell for x, row in enumerate(input) for y, cell in enumerate(list(row))}

    visited = set()
    regions = []
    for x, y in grid.keys():
        if (x, y) not in visited:
            regions.append(get_region(grid, x, y, visited))

    part1, part2 = 0, 0
    for region in regions:
        part1 += region.area * region.perimeter
        part2 += region.area * region.sides

    print("Part 1:", part1)
    print("Part 2:", part2)
