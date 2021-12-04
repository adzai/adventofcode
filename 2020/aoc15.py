def solve(starting_nums, limit):
    d = {k:v+1 for v, k in enumerate(starting_nums)}
    turn = len(list(d.keys())) + 1
    last_spoken = starting_nums[-1]

    while turn <= limit:
        diff = turn - 1 - d[last_spoken]
        d[last_spoken] = turn - 1
        if d.get(diff) is None:
            d[diff] = turn
        last_spoken = diff
        turn += 1
    return last_spoken

starting_nums = [1,0,15,2,10,13]
# starting_nums = [0,3,6]
# starting_nums = [3,1,2]

print("Part1:", solve(starting_nums, 2020))
print("Part2:", solve(starting_nums, 30000000))
