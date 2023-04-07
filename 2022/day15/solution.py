import re

with open("15.txt") as f:
    lines = f.read().split("\n")[:-1]


def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def smart_range(x, y):
    return list(range(min(x, y), max(x, y) + 1))


def cartesian(val1, val2):
    if isinstance(val1, list):
        return [(lst_val, val2) for lst_val in val1]
    return [(val1, lst_val) for lst_val in val2]


def get_line(point1, point2):
    points = []
    x1, y1 = point1[0], point1[1]
    x2, y2 = point2[0], point2[1]
    x_shift = 1 if x1 < x2 else -1
    y_shift = 1 if y1 < y2 else -1
    while x1 != x2 and y1 != y2:
        x1 += x_shift
        y1 += y_shift
        points.append((x1, y1))

    return points


class Solution:
    def __init__(self):
        self.sensors = {}
        self.smallest_x = float("inf")
        self.biggest_x = float("-inf")
        self.beacon_positions = {}

    def parse(self, lines):
        for line in lines:
            sensor_x, sensor_y, beacon_x, beacon_y = list(map(int, re.findall("-?[0-9]+", line)))
            sensor_x = sensor_x  # - scale_smallest_x
            sensor_y = sensor_y  # - scale_smallest_y
            beacon_x = beacon_x  # - scale_smallest_x
            beacon_y = beacon_y  # - scale_smallest_y
            manhattan_dist = manhattan_distance(sensor_x, sensor_y, beacon_x, beacon_y)
            self.sensors[(sensor_x, sensor_y)] = manhattan_dist
            self.smallest_x = min(self.smallest_x, sensor_x, beacon_x)
            self.biggest_x = max(self.biggest_x, sensor_x, beacon_x)
            self.beacon_positions[(beacon_x, beacon_y)] = True

    def part1(self):
        y = 2000000
        counter = 0
        for idx in range(int(self.smallest_x), int(self.biggest_x) + 1):
            can_be = True
            for key, val in self.sensors.items():
                sensor_x, sensor_y = key[0], key[1]
                manhattan_dist = manhattan_distance(sensor_x, sensor_y, idx, y)
                if manhattan_dist <= val and not self.beacon_positions.get((idx, y)):
                    can_be = False
                    break
            if not can_be:
                counter += 1

        print("Part 1:", counter)

    def part2(self):
        all_points = []
        for key, val in self.sensors.items():
            x, y = key[0], key[1]
            val += 1
            top = (x, y + val)
            bottom = (x, y - val)
            right = (x + val, y)
            left = (x - val, y)
            line1 = get_line(top, right)
            line2 = get_line(right, bottom)
            line3 = get_line(bottom, left)
            line4 = get_line(left, top)
            all_points.extend(line1)
            all_points.extend(line2)
            all_points.extend(line3)
            all_points.extend(line4)

        limit = 4000000
        for point in all_points:
            x, y = point[0], point[1]
            if x > limit + 1 or y > limit + 1 or x < 0 or y < 0:
                continue
            can_be = True
            for key, val in self.sensors.items():
                sensor_x, sensor_y = key[0], key[1]
                manhattan_dist = manhattan_distance(sensor_x, sensor_y, x, y)
                if manhattan_dist <= val:
                    can_be = False
                    break
            if can_be:
                print("Part 2:", point[0] * limit + point[1])
                break


solution = Solution()
solution.parse(lines)
solution.part1()
solution.part2()
