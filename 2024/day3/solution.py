import re


class Mul:
    def __init__(self):
        self.chars = ""
        self.x = 0
        self.y = 0
        self.parsed = False

    def parse_next(self, char):
        self.parsed = False
        match char:
            case "m" if self.chars == "":
                self.chars = "m"
            case "u" if self.chars == "m":
                self.chars = "mu"
            case "l" if self.chars == "mu":
                self.chars = "mul"
            case "(" if self.chars == "mul":
                self.chars = "mul("
            case "," if self.chars != "" and self._is_num(self.chars[-1]):
                self.chars += ","
            case ")" if self.chars != "" and self._is_num(self.chars[-1]):
                self.chars += ")"
                x, y = re.findall(r"\d+", self.chars)
                self.x, self.y = int(x), int(y)
                self.parsed = True
                self.chars = ""
            case char if (
                self.chars != ""
                and self._is_num(char)
                and (self.chars[-1] in "(," or self._is_num(self.chars[-1]))
            ):
                self.chars += char
            case _:
                self.chars = ""

    def _is_num(self, num):
        return num in "0123456789"


class Do:
    def __init__(self):
        self.chars = ""
        self.parsed = False

    def parse_next(self, char):
        self.parsed = False
        match char:
            case "d" if self.chars == "":
                self.chars = "d"
            case "o" if self.chars == "d":
                self.chars = "do"
            case "(" if self.chars == "do":
                self.chars = "do("
            case ")" if self.chars == "do(":
                self.chars = "do()"
                self.parsed = True
            case _:
                self.chars = ""


class Dont:
    def __init__(self):
        self.chars = ""
        self.parsed = False

    def parse_next(self, char):
        self.parsed = False
        match char:
            case "d" if self.chars == "":
                self.chars = "d"
            case "o" if self.chars == "d":
                self.chars = "do"
            case "n" if self.chars == "do":
                self.chars = "don"
            case "'" if self.chars == "don":
                self.chars = "don'"
            case "t" if self.chars == "don'":
                self.chars = "don't"
            case "(" if self.chars == "don't":
                self.chars = "don't("
            case ")" if self.chars == "don't(":
                self.chars = "don't()"
                self.parsed = True
            case _:
                self.chars = ""


def part1(input):
    total = 0
    mul_parser = Mul()
    for line in input:
        for token in line:
            mul_parser.parse_next(token)
            if mul_parser.parsed:
                total += mul_parser.x * mul_parser.y
    return total


def part2(input):
    in_do_block = True
    do_parser, dont_parser, mul_parser = Do(), Dont(), Mul()
    total = 0
    for line in input:
        for token in line:
            do_parser.parse_next(token)
            dont_parser.parse_next(token)
            mul_parser.parse_next(token)
            if do_parser.parsed:
                in_do_block = True
            elif dont_parser.parsed:
                in_do_block = False
            elif mul_parser.parsed:
                if in_do_block:
                    total += mul_parser.x * mul_parser.y

    return total


if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read().split("\n")[:-1]

    print("Part 1:", part1(input))
    print("Part 2:", part2(input))
