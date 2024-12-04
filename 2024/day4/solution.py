from collections import defaultdict


def is_in_bounds(row_idx, col_idx, row_bound, col_bound):
    return 0 <= row_idx < row_bound and 0 <= col_idx < col_bound


def check_part1(input, current_idx_row, current_idx_col, row_bound, col_bound):
    word = "XMAS"

    coordinate_offsets = [(x, y) for x in [-1, 0, 1] for y in [-1, 0, 1]]

    totals = defaultdict(int)
    for i in range(len(word)):
        for coordinate_offset in coordinate_offsets:
            if totals[coordinate_offset] != i:
                continue

            row_idx = current_idx_row + (coordinate_offset[0] * i)
            col_idx = current_idx_col + (coordinate_offset[1] * i)
            if is_in_bounds(row_idx, col_idx, row_bound, col_bound) and input[row_idx][col_idx] == word[i]:
                totals[coordinate_offset] += 1

    return sum([1 for x in totals.values() if x == len(word)])


def check_part2(input, current_idx_row, current_idx_col, row_bound, col_bound):
    if input[current_idx_row][current_idx_col] != "A":
        return 0

    values_to_check = [
        {(-1, -1): "M", (-1, 1): "S", (1, -1): "M", (1, 1): "S"},
        {(-1, -1): "S", (-1, 1): "S", (1, -1): "M", (1, 1): "M"},
        {(-1, -1): "S", (-1, 1): "M", (1, -1): "S", (1, 1): "M"},
        {(-1, -1): "M", (-1, 1): "M", (1, -1): "S", (1, 1): "S"},
    ]
    total = 0
    for values in values_to_check:
        found = True
        for coordinate_offset, letter in values.items():
            row_idx = current_idx_row + coordinate_offset[0]
            col_idx = current_idx_col + coordinate_offset[1]
            if not is_in_bounds(row_idx, col_idx, row_bound, col_bound) or input[row_idx][col_idx] != letter:
                found = False
                break

        if found:
            total += 1

    return total


if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read().split("\n")[:-1]

    part1_total, part2_total = 0, 0
    row_bound = len(input)
    col_bound = len(input[0])
    for row_idx, row in enumerate(input):
        for col_idx, val in enumerate(row):
            part1_total += check_part1(input, row_idx, col_idx, row_bound, col_bound)
            part2_total += check_part2(input, row_idx, col_idx, row_bound, col_bound)

    print("Part 1:", part1_total)
    print("Part 2:", part2_total)
