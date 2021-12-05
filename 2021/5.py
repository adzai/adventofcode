with open("5.input") as f:
    input = f.readlines()


class Line:
    def __init__(self, x1, x2, y1, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def __repr__(self):
        return f"Line(x1: {self.x1}, x2: {self.x2}, y1: {self.y1}, y2: {self.y2})"


def parse(input):
    lines = []
    highest_x = 0
    highest_y = 0
    for line in input:
        coords = line.split(" -> ")
        x1, y1 = map(int, coords[0].split(","))
        x2, y2 = map(int, coords[1].split(","))
        lines.append(Line(x1, x2, y1, y2))
        highest_x = max(highest_x, x1, x2)
        highest_y = max(highest_y, y1, y2)
    grid = []
    for _ in range(highest_y + 1):
        row = []
        for _ in range(highest_x + 1):
            row.append(".")
        grid.append(row)
    return grid, lines


def draw(grid, lines):
    for line in lines:
        if line.x1 == line.x2:
            r = range(min(line.y1, line.y2), max(line.y1, line.y2) + 1)
            for y in r:
                if grid[y][line.x1] == ".":
                    grid[y][line.x1] = 1
                else:
                    grid[y][line.x1] += 1

        elif line.y1 == line.y2:
            r = range(min(line.x1, line.x2), max(line.x1, line.x2) + 1)
            for x in r:
                if grid[line.y1][x] == ".":
                    grid[line.y1][x] = 1
                else:
                    grid[line.y1][x] += 1
        else:
            step_x = -1 if line.x1 > line.x2 else 1
            step_y = -1 if line.y1 > line.y2 else 1
            rx = range(line.x1, line.x2 + step_x, step_x)
            ry = range(line.y1, line.y2 + step_y, step_y)
            for x, y in zip(rx, ry):
                if grid[y][x] == ".":
                    grid[y][x] = 1
                else:
                    grid[y][x] += 1


def pretty_print(grid):
    for row in grid:
        print(" ".join(map(str, row)))
    print()


def count(grid):
    return sum(
        map(
            lambda row: sum(
                map(lambda field: isinstance(field, int) and field >= 2, row)
            ),
            grid,
        )
    )


grid, lines = parse(input)
draw(grid, lines)
# pretty_print(grid)
print("Part 2:", count(grid))
