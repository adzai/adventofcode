orig_lights = []
with open("./18.txt") as f:
    orig_lights = f.readlines()
    orig_lights = [list(x.strip()) for x in orig_lights]


stuck_lights = (
    (0, 0),
    (0, len(orig_lights[0]) - 1),
    (len(orig_lights) - 1, 0),
    (len(orig_lights) - 1, len(orig_lights[0]) - 1),
)


def light_on(start_row, start_col, lights):
    on = 0
    for i in range(max(0, start_col - 1), start_col + 2):
        for j in range(max(0, start_row - 1), start_row + 2):
            if j == start_row and i == start_col:
                continue
            else:
                try:
                    if lights[i][j] == "#":
                        on += 1
                except:
                    pass
    return (
        lights[start_col][start_row] == "#"
        and on in range(2, 4)
        or lights[start_col][start_row] == "."
        and on == 3
    )


def check_stuck_lights(row, col):
    for pair in stuck_lights:
        if col == pair[0] and row == pair[1]:
            return True
    return False


def make_new_grid(old_grid, part2=False):
    new_grid = []
    for col in range(len(old_grid)):
        row_grid = ""
        for row in range(len(old_grid[0])):
            if part2:
                stuck = check_stuck_lights(row, col)
                if stuck:
                    on = True
                else:
                    on = light_on(row, col, old_grid)
            else:
                on = light_on(row, col, old_grid)
            if on:
                row_grid += "#"
            else:
                row_grid += "."
        new_grid.append(row_grid)
    return new_grid


def sum_turned_on_lights(lights):
    return sum(map(lambda x: sum(map(lambda y: y == "#", x)), lights))


def animate(lights, part2=False, rounds=100):
    if part2:
        # Turn on all 4 stuck lights
        for pair in stuck_lights:
            lights[pair[0]][pair[1]] = "#"
    for _ in range(rounds):
        lights = make_new_grid(lights, part2=part2)
    return lights


print("Part 1:", sum_turned_on_lights(animate(orig_lights[:])))

print("Part 2:", sum_turned_on_lights(animate(orig_lights[:], part2=True)))
