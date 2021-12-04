with open("aoc3.txt") as f:
    lines = f.readlines()

def solve(right, is_down=False):
    down = 1
    right_step = right
    trees = 0
    for line in lines:
        line = line.strip()
        l = line
        last_index = len(line) - 1
        if (is_down and down % 2 == 0) or down == 1:
            down += 1
            continue
        while right > last_index:
            l += line
            last_index += len(line) - 1
        if l[right] == "#":
            trees += 1
        right += right_step
        down += 1
    return trees

print(solve(1) *
      solve(3) *
      solve(5) *
      solve(7) *
      solve(1, is_down=True))
