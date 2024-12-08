from collections import defaultdict


def is_in_bounds(x, y, x_bound, y_bound):
    return 0 <= x and x < x_bound and 0 <= y and y < y_bound


def solve(grid: list[list[str]], antennas: dict[str, list[tuple]], part1: bool) -> int:
    x_bound, y_bound = len(grid), len(grid[0])
    antinodes = set()
    for coords in antennas.values():
        for i in range(len(coords)):
            for j in range(len(coords)):
                if i == j:
                    break

                if not part1:
                    antinodes.add(coords[i])
                    antinodes.add(coords[j])

                distance = (coords[i][0] - coords[j][0], coords[i][1] - coords[j][1])

                first_antinode_direction = (coords[i][0] + distance[0], coords[i][1] + distance[1])
                while is_in_bounds(first_antinode_direction[0], first_antinode_direction[1], x_bound, y_bound):
                    antinodes.add(first_antinode_direction)
                    if part1:
                        break

                    first_antinode_direction = (
                        first_antinode_direction[0] + distance[0],
                        first_antinode_direction[1] + distance[1],
                    )

                second_antinode_direction = (coords[j][0] - distance[0], coords[j][1] - distance[1])
                while is_in_bounds(second_antinode_direction[0], second_antinode_direction[1], x_bound, y_bound):
                    antinodes.add(second_antinode_direction)

                    if part1:
                        break
                    second_antinode_direction = (
                        second_antinode_direction[0] - distance[0],
                        second_antinode_direction[1] - distance[1],
                    )

    return len(antinodes)


if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read().split("\n")[:-1]

    grid = [list(row) for row in input]
    antennas = defaultdict(list)
    for i, row in enumerate(input):
        for j, cell in enumerate(row):
            if cell != ".":
                antennas[cell].append((i, j))

    print("Part 1:", solve(grid, antennas, part1=True))
    print("Part 2:", solve(grid, antennas, part1=False))
