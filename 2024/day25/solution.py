MAX_HEIGHT = 5


def get_locks_and_keys(input_data):
    locks, keys = [], []
    for grid in input_data:
        grid = list(filter(lambda x: x != "", grid.split("\n")))
        if grid[0][0] == "#":
            is_lock = True
        else:
            is_lock = False
        inner = []
        for x in range(len(grid[0])):
            col = []
            for y in range(len(grid)):
                if grid[y][x] == "#":
                    col.append(y)
            if is_lock:
                inner.append(max(col))
            else:
                inner.append(len(grid) - 1 - min(col))

        if is_lock:
            locks.append(inner)
        else:
            keys.append(inner)

    return locks, keys


if __name__ == "__main__":
    with open("input.txt") as f:
        input_data = f.read().split("\n\n")

    locks, keys = get_locks_and_keys(input_data)

    print(
        "Result:",
        sum(
            [
                1
                for lock in locks
                for key in keys
                if all(lock_col + key_col <= MAX_HEIGHT for lock_col, key_col in zip(lock, key))
            ]
        ),
    )
