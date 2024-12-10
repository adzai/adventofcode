UP, DOWN, LEFT, RIGHT = (-1, 0), (1, 0), (0, -1), (0, 1)


def is_in_bounds(x, y, x_bound, y_bound):
    return 0 <= x and x < x_bound and 0 <= y and y < y_bound


def solve(part1: bool):
    trailheads = []
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == "0":
                trailheads.append((i, j))

    directions = [UP, DOWN, LEFT, RIGHT]
    x_bound, y_bound = len(grid), len(grid[0])
    total = 0
    for trailhead in trailheads:
        nodes_to_visit = [trailhead]
        visited, unique_nines_reached, nines_reached_count = set(), set(), 0
        while len(nodes_to_visit) > 0:
            current_x, current_y = nodes_to_visit.pop(0)
            target = str(int(grid[current_x][current_y]) + 1)

            if (current_x, current_y) in visited:
                continue

            if part1:
                visited.add((current_x, current_y))

            for dir in directions:
                new_x, new_y = current_x + dir[0], current_y + dir[1]
                if is_in_bounds(new_x, new_y, x_bound, y_bound) and grid[new_x][new_y] == target:
                    if target == "9":
                        unique_nines_reached.add((new_x, new_y))
                        nines_reached_count += 1
                    else:
                        nodes_to_visit.append((new_x, new_y))

        if part1:
            total += len(unique_nines_reached)
        else:
            total += nines_reached_count

    return total


if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read().split("\n")[:-1]

    grid = [list(row) for row in input]

    print("Part 1:", solve(part1=True))
    print("Part 2:", solve(part1=False))
