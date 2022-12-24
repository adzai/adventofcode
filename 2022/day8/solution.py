with open("input.txt") as f:
    grid = list(map(list, f.read().split("\n")[:-1]))

max_row = len(grid[0])
max_col = len(grid)


def is_edge(x, y):
    return x == 0 or y == 0 or x == max_row - 1 or y == max_col - 1


def is_visible_x(val, x, y, step, x_bound):
    ctr = 1
    while x != x_bound:
        if val <= grid[y][x]:
            return False, ctr
        else:
            x += step
            ctr += 1

    return True, ctr


def is_visible_y(val, x, y, step, y_bound):
    ctr = 1
    while y != y_bound:
        if val <= grid[y][x]:
            return False, ctr
        else:
            y += step
            ctr += 1

    return True, ctr


def part1():
    visible_trees = 0
    for y, col in enumerate(grid):
        for x, val in enumerate(col):
            if is_edge(x, y):
                visible_trees += 1
                continue

            up_visibility, _ = is_visible_y(val, x, y - 1, -1, -1)
            if up_visibility:
                visible_trees += 1
                continue

            down_visibility, _ = is_visible_y(val, x, y + 1, 1, max_col)
            if down_visibility:
                visible_trees += 1
                continue

            left_visibility, _ = is_visible_x(val, x - 1, y, -1, -1)
            if left_visibility:
                visible_trees += 1
                continue

            right_visibility, _ = is_visible_x(val, x + 1, y, 1, max_row)
            if right_visibility:
                visible_trees += 1

    print("Part 1:", visible_trees)


def part2():
    maximum_score = 0
    for y, col in enumerate(grid):
        for x, val in enumerate(col):
            total_score = 1
            if is_edge(x, y):
                continue
            # up
            _, up_score = is_visible_y(val, x, y - 1, -1, 0)
            # left
            _, left_score = is_visible_x(val, x - 1, y, -1, 0)
            # down
            _, down_score = is_visible_y(val, x, y + 1, 1, max_col - 1)
            # right
            _, right_score = is_visible_x(val, x + 1, y, 1, max_row - 1)
            total_score = up_score * left_score * down_score * right_score
            if total_score > maximum_score:
                maximum_score = total_score

    print("Part 2:", maximum_score)


part1()
part2()
