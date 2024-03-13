def update_current_coordinates(current_coords, increment_coords):
    increment_idx = 0 if increment_coords[0] != 0 else 1
    current_coords[increment_idx] += increment_coords[increment_idx]


def solve(input, part2=False):
    direction_to_coord_increment = {0: (0, 1), 1: (1, 0), 2: (0, -1), 3: (-1, 0)}

    current_direction = 0
    current_coords = [0, 0]
    turn_to_rotation_change = {"L": -1, "R": 1}
    visited_coords = set()
    for command in input:
        turn, value = command[0], int(command[1:])
        rotation = turn_to_rotation_change[turn]
        current_direction = (current_direction + rotation) % 4
        increment_coords = direction_to_coord_increment[current_direction]

        for _ in range(value):
            update_current_coordinates(current_coords, increment_coords)
            if part2:
                if tuple(current_coords) in visited_coords:
                    return abs(current_coords[0]) + abs(current_coords[1])
                else:
                    visited_coords.add(tuple(current_coords))

    return abs(current_coords[0]) + abs(current_coords[1])


if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read().replace(",", "").split(" ")

    print("Part 1:", solve(input))
    print("Part 2:", solve(input, part2=True))
