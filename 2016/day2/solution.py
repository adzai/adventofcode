def clip_position(current_val, increment, keypad):
    KEYPAD_BOUND_IDX = len(keypad[0])

    if current_val + increment < 0 or current_val + increment >= KEYPAD_BOUND_IDX:
        return current_val

    return current_val + increment


def solve(input, keypad, current_position):
    direction_to_position_increment = {"U": (-1, 0), "R": (0, 1), "D": (1, 0), "L": (0, -1)}
    combination = ""
    LOWER_BOUND, UPPER_BOUND = 0, len(keypad[0])
    for line in input:
        for direction in line:
            increment = direction_to_position_increment[direction]
            new_position_row = current_position[0] + increment[0]
            new_position_col = current_position[1] + increment[1]

            if (
                new_position_row < LOWER_BOUND
                or new_position_row >= UPPER_BOUND
                or new_position_col < LOWER_BOUND
                or new_position_col >= UPPER_BOUND
            ):
                continue
            if keypad[new_position_row][new_position_col] is not None:
                current_position = [new_position_row, new_position_col]

        combination += keypad[current_position[0]][current_position[1]]

    return combination


if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read().split("\n")[:-1]

    part1_keypad = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
    print("Part 1:", solve(input, part1_keypad, [1, 1]))
    part2_keypad = [
        [None, None, "1", None, None],
        [None, "2", "3", "4", None],
        ["5", "6", "7", "8", "9"],
        [None, "A", "B", "C", None],
        [None, None, "D", None, None],
    ]
    print("Part 2:", solve(input, part2_keypad, [2, 0]))
