DIRECTIONS = (-1, 0), (1, 0), (0, -1), (0, 1)
MAX_PICOSECONDS = 100


def is_in_bounds(x, y, grid):
    return 0 < x < len(grid) - 1 and 0 < y < len(grid[0]) - 1


def get_number_of_cheats(path, max_allowed_cheat_distance):
    available_cheats = 0
    for i, coordinates in enumerate(path):
        target_picoseconds = MAX_PICOSECONDS
        for potential_cheat_destination_coordinates in path[i + MAX_PICOSECONDS :]:
            distance_to_potential_cheat = abs(coordinates[0] - potential_cheat_destination_coordinates[0]) + abs(
                coordinates[1] - potential_cheat_destination_coordinates[1]
            )

            if (
                distance_to_potential_cheat <= max_allowed_cheat_distance
                and target_picoseconds - distance_to_potential_cheat >= MAX_PICOSECONDS
            ):
                available_cheats += 1

            target_picoseconds += 1

    return available_cheats


def find_path(grid, starting_position, ending_position):
    queue = [(starting_position[0], starting_position[1], [])]
    visited = set()
    while len(queue) > 0:
        x, y, path = queue.pop(0)
        grid[x][y] = "O"

        if (x, y) == ending_position:
            return path + [ending_position]

        if (x, y) in visited:
            continue

        visited.add((x, y))

        for direction in DIRECTIONS:
            new_x, new_y = (x + direction[0], y + direction[1])
            if is_in_bounds(new_x, new_y, grid) and grid[new_x][new_y] != "#":
                queue.append((new_x, new_y, path + [(x, y)]))

    raise Exception("Couldn't find a path")


if __name__ == "__main__":
    with open("input.txt") as f:
        input_data = f.read().split("\n")[:-1]

    grid = [list(row) for row in input_data]

    starting_position, ending_position = None, None

    for x, row in enumerate(grid):
        for y, cell in enumerate(row):
            if cell == "S":
                starting_position = (x, y)
            elif cell == "E":
                ending_position = (x, y)

    assert starting_position is not None and ending_position is not None

    path = find_path(grid, starting_position, ending_position)

    print("Part 1:", get_number_of_cheats(path, 2))
    print("Part 2:", get_number_of_cheats(path, 20))
