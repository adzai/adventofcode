UP = (-1, 0)


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_right_turn(self):
        return Position(self.y, -self.x)

    def __add__(self, other):
        return Position(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __repr__(self):
        return str(self.x) + "," + str(self.y)


class Guard:
    def __init__(self, position, direction):
        self.position = position
        self.direction = direction

    def get_guards_state(self):
        return (self.position, self.direction)

    def get_new_position(self):
        return self.position + self.direction

    def move_to_new_position(self):
        self.position = self.get_new_position()

    def turn_right(self):
        self.direction = self.direction.get_right_turn()


class Lab:
    def __init__(self, map, starting_position, debug=False):
        self.map = map
        self.debug = debug
        self.starting_position = starting_position
        self.guard = Guard(starting_position, Position(*UP))
        self.unique_visited_states, self.unique_visited_locations, self.obstacles = set(), set(), set()

    def reset_guard(self):
        self.guard = Guard(self.starting_position, Position(*UP))

    def remove_drawings_from_map(self):
        for i, row in enumerate(self.map):
            for j, cell in enumerate(row):
                if cell in "XG":
                    self.map[i][j] = "."

        self.map[self.starting_position.x][self.starting_position.y] = "^"

    def get_guards_square_value(self):
        return self.map[self.guard.position.x][self.guard.position.y]

    def draw_on_map(self, position, char):
        self.map[position.x][position.y] = char

    def place_obstacle(self, obstacle_position):
        self.map[obstacle_position.x][obstacle_position.y] = "#"

    def remove_obstacle(self, obstacle_position):
        self.map[obstacle_position.x][obstacle_position.y] = "."

    def run(self):
        self.add_visit()
        while self.move_guard_on_map_once():
            self.add_visit()

        print("Part 1:", len(self.unique_visited_locations))
        if self.debug: self.remove_drawings_from_map()

    def solve(self):
        self.run()
        states_before_obstacle = self.unique_visited_states
        for state in states_before_obstacle:
            self.reset()
            obstacle_position = state[0] + state[1]
            if (
                obstacle_position != self.starting_position
                and self.is_in_bounds(obstacle_position)
                and self.map[obstacle_position.x][obstacle_position.y] != "#"
            ):
                self.place_obstacle(obstacle_position)
                while self.move_guard_on_map_once():
                    if self.guard.get_guards_state() in self.unique_visited_states:
                        self.obstacles.add(obstacle_position)
                        break
                    self.add_visit()
                self.remove_obstacle(obstacle_position)

        print("Part 2:", len(self.obstacles))

    def reset(self):
        self.guard = Guard(self.starting_position, Position(*UP))
        self.unique_visited_states = set((self.guard.get_guards_state(),))

        self.unique_visited_locations = set((self.guard.position,))

    def add_visit(self):
        self.unique_visited_states.add(self.guard.get_guards_state())

        self.unique_visited_locations.add(self.guard.position.__repr__())

    def move_guard_on_map_once(self):
        new_position = self.guard.get_new_position()
        if not self.is_in_bounds(new_position):
            return False

        if self.map[new_position.x][new_position.y] == "#":
            self.guard.turn_right()
        else:
            if self.debug: self.draw_on_map(self.guard.position, "X")
            self.guard.move_to_new_position()
            if self.debug: self.draw_on_map(self.guard.position, "G")

        return True

    def is_in_bounds(self, position):
        return 0 <= position.x < len(self.map) and 0 <= position.y < len(self.map[0])

    def __repr__(self):
        return "\n".join(["".join(x) for x in self.map])


if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read().split("\n")[:-1]

    input = [list(x) for x in input]
    starting_guard_position = None
    for i, row in enumerate(input):
        for j, col in enumerate(row):
            if col == "^":
                starting_guard_position = Position(i, j)
                break
        if starting_guard_position is not None:
            break

    assert starting_guard_position is not None

    Lab(input, starting_guard_position, debug=False).solve()
