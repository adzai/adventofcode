with open("7.input") as f:
    input = sorted(map(int, f.read().split(",")))


def solve(input, part2=False):
    spread = 25
    prev_result = None
    while True:
        result = solve_helper(input, spread, part2)
        if result == prev_result:
            return result
        prev_result = result
        spread *= 2


def solve_helper(input, spread, part2):
    mid = len(input) // 2
    pivots = [
        input[i] for i in range(max(0, mid - spread), min(mid + spread, len(input)))
    ]
    pivot_range = range(pivots[0], pivots[-1] + 1)
    lowest_sum = None
    for pivot in pivot_range:
        current_sum = 0
        for num in input:
            steps = abs(num - pivot)
            if part2:
                gauss = steps * (steps + 1) // 2
                current_sum += gauss
            else:
                current_sum += steps
        if lowest_sum is None or current_sum < lowest_sum:
            lowest_sum = current_sum
    return lowest_sum


print("Part 1:", solve(input))
print("Part 2:", solve(input, part2=True))
