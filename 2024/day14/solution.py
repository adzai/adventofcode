from collections import defaultdict

WIDTH, HEIGHT = 101, 103


def is_in_bounds(x, y):
    return 0 <= x < HEIGHT and 0 <= y < WIDTH


class Velocity:
    def __init__(self, y, x):
        self.x = x
        self.y = y


class Position:
    def __init__(self, y, x):
        assert is_in_bounds(x, y), f"x: {x}, y: {y}"
        self.x = x
        self.y = y


class Robot:
    def __init__(self, position: Position, velocity: Velocity):
        self.position = position
        self.velocity = velocity


def init_robots(input_data):
    robots = defaultdict(list)
    for line in input_data:
        p, v = line.split(" ")
        p1, p2 = p.split(",")
        v1, v2 = v.split(",")
        robot = Robot(Position(int(p1.replace("p=", "")), int(p2)), Velocity(int(v1.replace("v=", "")), int(v2)))
        robots[(robot.position.x, robot.position.y)].append(robot)

    return robots


def print_grid(robots):
    for x in range(HEIGHT):
        for y in range(WIDTH):
            if (num_of_robots := len(robots[(x, y)])) > 0:
                print(num_of_robots, end="")
            else:
                print(".", end="")
        print("")


def get_part1_safety_score(robots):
    number_of_robots_in_quadrants = defaultdict(int)
    for x in range(HEIGHT):
        if x == HEIGHT // 2:
            continue
        for y in range(WIDTH):
            if y == WIDTH // 2:
                continue
            number_of_robots_in_quadrants[(x < HEIGHT // 2, y < WIDTH // 2)] += len(robots[(x, y)])

    vals = list(number_of_robots_in_quadrants.values())
    safety_score = vals[0]
    for v in vals[1:]:
        safety_score *= v

    return safety_score


def has_neighbors_in_all_directions(robots, x, y):
    coordinates_offsets = [(x, y) for x in [-1, 0, 1] for y in [-1, 0, 1]]
    for coordinates_offset in coordinates_offsets:
        pos_to_check = (x + coordinates_offset[0], y + coordinates_offset[1])
        if (robots_at_coordinates := robots.get(pos_to_check)) is None or len(robots_at_coordinates) == 0:
            return False

    return True


def move_robots(robots, part2=False):
    second = 1
    while True:
        new_robot_positions = defaultdict(list)
        for robot_coordinates in robots.keys():
            robots_at_coordinate = robots[robot_coordinates]
            while robots_at_coordinate:
                robot = robots_at_coordinate.pop()
                new_position = Position(
                    (robot.position.y + robot.velocity.y) % WIDTH, (robot.position.x + robot.velocity.x) % HEIGHT
                )
                robot.position = new_position
                new_robot_positions[(robot.position.x, robot.position.y)].append(robot)

        robots = new_robot_positions
        if part2 and any(
            [
                has_neighbors_in_all_directions(robots, robot.position.x, robot.position.y)
                for robots_at_coordinates in robots.values()
                for robot in robots_at_coordinates
            ]
        ):
            print_grid(robots)

            return second

        if not part2 and second == 100:
            break

        second += 1

    return robots


if __name__ == "__main__":
    with open("input.txt") as f:
        input_data = f.read().split("\n")[:-1]

    robots = init_robots(input_data)
    robots = move_robots(robots)
    print("Part 1:", get_part1_safety_score(robots))

    robots = init_robots(input_data)
    print("Part 2:", move_robots(robots, part2=True))
