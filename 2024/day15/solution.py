MOVE_TO_DIRECTION_OFFSET = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}


def is_in_bounds(grid, x, y):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0])


def get_robot_coordinates_from_grid(grid):
    robot_coordinates = None
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == "@":
                robot_coordinates = (x, y)
                break

    assert robot_coordinates is not None

    return robot_coordinates


def handle_boxes_part1(grid, robot_coordinates, new_robot_coordinates, move_direction):
    grid_space = grid[new_robot_coordinates[0]][new_robot_coordinates[1]]
    if grid_space == "O":
        box_coordinates = new_robot_coordinates
        while grid[box_coordinates[0]][box_coordinates[1]] == "O":
            box_coordinates = (
                box_coordinates[0] + move_direction[0],
                box_coordinates[1] + move_direction[1],
            )
        new_space = grid[box_coordinates[0]][box_coordinates[1]]
        if new_space == ".":
            grid[box_coordinates[0]][box_coordinates[1]] = "O"
            grid[robot_coordinates[0]][robot_coordinates[1]] = "."
            grid[new_robot_coordinates[0]][new_robot_coordinates[1]] = "@"
            robot_coordinates = new_robot_coordinates

    return robot_coordinates


def handle_boxes_part2(grid, robot_coordinates, new_robot_coordinates, move_direction):
    grid_space = grid[new_robot_coordinates[0]][new_robot_coordinates[1]]
    if grid_space not in "[]":
        return robot_coordinates

    box_coordinates = (
        ((new_robot_coordinates[0], new_robot_coordinates[1] - 1), new_robot_coordinates)
        if grid_space == "]"
        else (new_robot_coordinates, (new_robot_coordinates[0], new_robot_coordinates[1] + 1))
    )
    old_boxes_coordinates, new_boxes_coordinates, collision_with_wall = (
        get_old_boxes_and_new_boxes_and_collision_with_wall(grid, box_coordinates, move_direction)
    )
    if collision_with_wall:
        return robot_coordinates

    for neighbor in old_boxes_coordinates:
        left, right = neighbor
        grid[left[0]][left[1]] = "."
        grid[right[0]][right[1]] = "."

    for neighbor in new_boxes_coordinates:
        left, right = neighbor
        grid[left[0]][left[1]] = "["
        grid[right[0]][right[1]] = "]"

    grid[robot_coordinates[0]][robot_coordinates[1]] = "."
    grid[new_robot_coordinates[0]][new_robot_coordinates[1]] = "@"

    return new_robot_coordinates


def move_robot_around_grid(grid, robot_moves, robot_coordinates, handle_boxes):
    for move in robot_moves:
        new_robot_coordinates = (
            robot_coordinates[0] + MOVE_TO_DIRECTION_OFFSET[move][0],
            robot_coordinates[1] + MOVE_TO_DIRECTION_OFFSET[move][1],
        )
        grid_space = grid[new_robot_coordinates[0]][new_robot_coordinates[1]]

        if grid_space == ".":
            grid[robot_coordinates[0]][robot_coordinates[1]] = "."
            grid[new_robot_coordinates[0]][new_robot_coordinates[1]] = "@"
            robot_coordinates = new_robot_coordinates

        robot_coordinates = handle_boxes(grid, robot_coordinates, new_robot_coordinates, MOVE_TO_DIRECTION_OFFSET[move])


def generate_wide_grid(input_grid):
    new_grid = [list(row) for row in input_grid.split("\n")]
    wide_grid = []
    x, y = 0, 0
    for x in range(len(new_grid)):
        inner_grid = []
        for y in range(len(new_grid[0])):
            match new_grid[x][y]:
                case "O":
                    inner_grid.append("[")
                    inner_grid.append("]")
                case "#":
                    inner_grid.append("#")
                    inner_grid.append("#")
                case "@":
                    inner_grid.append("@")
                    inner_grid.append(".")
                case ".":
                    inner_grid.append(".")
                    inner_grid.append(".")
                case _:
                    raise Exception(f"Couldn't parse {new_grid[x][y]}")

        wide_grid.append(inner_grid)

    return wide_grid


def get_old_boxes_and_new_boxes_and_collision_with_wall(
    grid, current_coordinates: tuple[tuple[int, int], tuple[int, int]], direction_to_move_in
):
    coordinates_to_visit, old_boxes_coordinates = [current_coordinates], [current_coordinates]
    visited = set()
    while len(coordinates_to_visit) > 0:
        current_whole_box_coordinates = coordinates_to_visit.pop(0)
        if current_whole_box_coordinates in visited:
            continue

        visited.add(current_whole_box_coordinates)
        for current_box_part_coordinates in current_whole_box_coordinates:
            new_box_coordinates_to_check = (
                current_box_part_coordinates[0] + direction_to_move_in[0],
                current_box_part_coordinates[1] + direction_to_move_in[1],
            )
            grid_space = grid[new_box_coordinates_to_check[0]][new_box_coordinates_to_check[1]]
            if (
                not is_in_bounds(grid, new_box_coordinates_to_check[0], new_box_coordinates_to_check[1])
                or grid_space not in "[]"
            ):
                continue

            whole = (
                ((new_box_coordinates_to_check[0], new_box_coordinates_to_check[1] - 1), new_box_coordinates_to_check)
                if grid_space == "]"
                else (
                    new_box_coordinates_to_check,
                    (new_box_coordinates_to_check[0], new_box_coordinates_to_check[1] + 1),
                )
            )
            coordinates_to_visit.append(whole)
            old_boxes_coordinates.append(whole)

    new_boxes_coordinates = []
    for old_box_coordinates in list(set(old_boxes_coordinates)):
        left_box_part_coordinates, right_box_part_coordinates = old_box_coordinates
        new_box_coordinates = (
            (
                left_box_part_coordinates[0] + direction_to_move_in[0],
                left_box_part_coordinates[1] + direction_to_move_in[1],
            ),
            (
                right_box_part_coordinates[0] + direction_to_move_in[0],
                right_box_part_coordinates[1] + direction_to_move_in[1],
            ),
        )
        if (
            grid[new_box_coordinates[0][0]][new_box_coordinates[0][1]] == "#"
            or grid[new_box_coordinates[1][0]][new_box_coordinates[1][1]] == "#"
        ):
            return list(set(old_boxes_coordinates)), list(set(old_boxes_coordinates)), True
        new_boxes_coordinates.append(new_box_coordinates)

    return list(set(old_boxes_coordinates)), new_boxes_coordinates, False

def part1(input_grid, robot_moves):
    grid = [list(row) for row in input_grid.split("\n")]

    move_robot_around_grid(grid, robot_moves, get_robot_coordinates_from_grid(grid), handle_boxes_part1)

    final_gps_coordinates = 0
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == "O":
                final_gps_coordinates += 100 * x + y

    return final_gps_coordinates

def part2(input_grid, robot_moves):
    wide_grid = generate_wide_grid(input_grid)

    move_robot_around_grid(wide_grid, robot_moves, get_robot_coordinates_from_grid(wide_grid), handle_boxes_part2)

    final_gps_coordinates = 0
    for x in range(len(wide_grid)):
        y = 0
        while y < len(wide_grid[0]):
            if wide_grid[x][y] == "[":
                final_gps_coordinates += 100 * x + y
                y += 1
            y += 1

    return final_gps_coordinates


if __name__ == "__main__":
    with open("input.txt") as f:
        input_grid, instructions = f.read().split("\n\n")
    robot_moves = "".join(instructions.split("\n")[:-1])

    print("Part 1:", part1(input_grid, robot_moves))
    print("Part 2:", part2(input_grid, robot_moves))
