import math

with open("11.txt") as f:
    blocks = f.read().split("\n\n")


class Monkey:
    def __init__(self):
        self.items = None
        self.operation = None
        self.test = None
        self.true = None
        self.false = None
        self.counter = 0


class Interpreter:
    def __init__(self):
        self.monkeys = []

    def parse(self, blocks):
        for i, block in enumerate(blocks):
            for j, line in enumerate(block.split("\n")):
                if j == 0:
                    self.monkeys.append(Monkey())
                elif j == 1:
                    items = list(map(lambda x: int(x), line.replace("Starting items: ", "").split(", ")))
                    self.monkeys[i].items = items
                elif j == 2:
                    self.monkeys[i].operation = Interpreter._eval(line)
                elif j == 3:
                    self.monkeys[i].test = int(line.split(" ")[-1])
                elif j == 4:
                    self.monkeys[i].true = int(line.split(" ")[-1])
                elif j == 5:
                    self.monkeys[i].false = int(line.split(" ")[-1])

    @staticmethod
    def _eval(line):
        return lambda x: eval(line.replace("Operation: new = ", "").strip().replace("old", str(x)))

    def play_round(self, part2, supermodulo=None):
        for i, monkey in enumerate(self.monkeys):
            for item in monkey.items:
                self.monkeys[i].counter += 1
                new = monkey.operation(item)
                if part2:
                    new_item = new % supermodulo
                else:
                    new_item = new // 3
                if new_item % monkey.test == 0:
                    self.monkeys[monkey.true].items.append(new_item)
                else:
                    self.monkeys[monkey.false].items.append(new_item)
            self.monkeys[i].items = []

    def get_puzzle_result(self):
        counters = [monkey.counter for monkey in self.monkeys]
        first_max = max(counters)
        counters.remove(first_max)
        second_max = max(counters)

        return first_max * second_max


def get_chinese_remainder_theorem_supermodulo(monkeys):
    elements = [monkey.test for monkey in monkeys]

    return math.prod(elements)


def part1():
    interpreter = Interpreter()
    interpreter.parse(blocks)
    for _ in range(20):
        interpreter.play_round(part2=False)
    print("Part 1:", interpreter.get_puzzle_result())


def part2():
    interpreter = Interpreter()
    interpreter.parse(blocks)
    supermodulo = get_chinese_remainder_theorem_supermodulo(interpreter.monkeys)
    for _ in range(10000):
        interpreter.play_round(part2=True, supermodulo=supermodulo)
    print("Part 2:", interpreter.get_puzzle_result())


part1()
part2()
