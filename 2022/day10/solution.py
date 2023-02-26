with open("10.txt") as f:
    instructions = f.read().split("\n")[:-1]


class Instruction:
    def __init__(self, instruction):
        self.remaining_cycles = 1 if instruction == "noop" else 2
        self.add_value = 0 if instruction == "noop" else int(instruction.split()[-1])

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n < self.remaining_cycles:
            self.n += 1
            return 1
        else:
            raise StopIteration


def part1():
    clock = 0
    clock_checkpoint = 20
    register_X = 1
    max_strength = 0

    for instruction in instructions:
        instruction = Instruction(instruction)
        for elapsed_cycle in instruction:
            clock += elapsed_cycle
            if clock == clock_checkpoint:
                max_strength += clock * register_X
                clock_checkpoint += 40

        register_X += instruction.add_value

    print("Part 1:", max_strength)


def part2():
    width = 40
    height = 6
    screen = ["."] * height * width
    clock = -1  # to avoid off by one on the screen
    register_X = 1

    for instruction in instructions:
        instruction = Instruction(instruction)
        for elapsed_cycle in instruction:
            clock += elapsed_cycle
            if register_X in range(clock % 40 - 1, clock % 40 + 2):
                screen[clock] = "#"

        register_X += instruction.add_value

    slice = width
    print("Part 2:")
    for _ in range(height):
        print("".join(screen[slice - width : slice]))
        slice += width


part1()
part2()
