with open("input.txt") as f:
    input = list(map(lambda x: x.strip("\n"), f.readlines()))


def move(pos, head, tail):
    if head[pos] > tail[pos]:
        tail[pos] += 1
    else:
        tail[pos] -= 1


def adjust_position(head, tail):
    cond_x = abs(head[0] - tail[0]) > 1
    cond_y = abs(head[1] - tail[1]) > 1
    cond_not_same = head[0] != tail[0] and head[1] != tail[1]

    if (cond_x or cond_y) and cond_not_same:
        move(0, head, tail)
        move(1, head, tail)
    else:
        if cond_x:
            move(0, head, tail)
        if cond_y:
            move(1, head, tail)


def get_unique_visited_by_tail(size):
    visited = {}
    rope = [[0, 0] for _ in range(size)]
    visited[tuple(rope[-1])] = True

    for instruction in input:
        direction, steps = instruction.split()
        steps = int(steps)
        if direction == "R":
            y_step, x_step = 0, 1
        elif direction == "L":
            y_step, x_step = 0, -1
        elif direction == "U":
            y_step, x_step = -1, 0
        elif direction == "D":
            y_step, x_step = 1, 0
        else:
            raise Exception("Unknown direction")

        while steps != 0:
            rope[0][0] += x_step
            rope[0][1] += y_step
            for i in range(1, len(rope)):
                adjust_position(rope[i - 1], rope[i])
                if i + 1 == len(rope):
                    visited[tuple(rope[i])] = True
            steps -= 1

    return len(visited.keys())


print(get_unique_visited_by_tail(2))
print(get_unique_visited_by_tail(10))
