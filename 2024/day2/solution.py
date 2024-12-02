class Level:
    def __init__(self, row: list[int], faults=0):
        self.slope = None
        self.row = list(map(lambda val: int(val), row))
        self.prev_vals = []
        self.faults = faults

    def is_level_safe(self):
        self.prev_vals.append(self.row[0])

        for i, val in enumerate(self.row[1:], 1):
            is_safe = self.is_value_safe(val)
            if not is_safe and self.faults == 0:
                for j in range(max(i - 2, 0), i + 1):
                    ret = Level(self.row[:j] + self.row[j + 1 :], faults=1).is_level_safe()

                    if ret:
                        return True

                return False
            elif not is_safe:
                return False

        return True

    def is_value_safe(self, current_val):
        prev_val = self.prev_vals[-1]
        if self.slope == None:
            if current_val > prev_val:
                self.slope = lambda x: x > 0
            else:
                self.slope = lambda x: x < 0

        diff = abs(current_val - prev_val)

        self.prev_vals.append(current_val)
        return self.slope(current_val - prev_val) and 1 <= diff <= 3


if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read().split("\n")[:-1]

    print("Part 1:", sum([Level(list(map(lambda val: int(val), row.split())), faults=1).is_level_safe() for row in input]))
    print("Part 2:", sum([Level(list(map(lambda val: int(val), row.split()))).is_level_safe() for row in input]))
