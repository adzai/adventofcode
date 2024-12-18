WIDTH, HEIGHT = 71, 71
# WIDTH, HEIGHT = 7, 7
DIRECTIONS = (-1, 0), (1, 0), (0, -1), (0, 1)


def is_in_bounds(x, y):
    return 0 <= x < HEIGHT and 0 <= y < WIDTH


def get_grid():
    grid = []
    for _ in range(HEIGHT):
        inner = []
        for _ in range(WIDTH):
            inner.append(".")
        grid.append(inner)

    return grid


def simulate_falls(grid, limit):
    for line in input_data[:limit]:
        y, x = line.split(",")
        grid[int(x)][int(y)] = "#"

def solve(input_data, part2):
    nanosecond = 1024
    while True:
        grid = get_grid()
        simulate_falls(grid, nanosecond)
        queue = [(0, 0, 0, [])]
        visited = set()
        completed_paths = []
        while len(queue) > 0:
            x, y, steps, path = queue.pop(0)

            if (x, y) == (HEIGHT - 1, WIDTH - 1):
                if not part2:
                    return steps

                completed_paths.append(list(set(path)))

            if (x, y) in visited:
                continue

            visited.add((x, y))

            for direction in DIRECTIONS:
                new_x, new_y = (x + direction[0], y + direction[1])
                if is_in_bounds(new_x, new_y) and grid[new_x][new_y] == ".":
                    queue.append((new_x, new_y, steps + 1, path + [(x, y)]))

        if len(completed_paths) == 0:
            return input_data[nanosecond - 1]

        nanosecond += 1

if __name__ == "__main__":
    with open("input.txt") as f:
        input_data = f.read().split("\n")[:-1]
    
    print("Part 1:", solve(input_data, part2=False))
    print("Part 2:", solve(input_data, part2=True))
