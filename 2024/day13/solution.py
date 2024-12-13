import re


def solve(input, part2=False):
    idx, tokens = 0, 0
    while idx < len(input):
        block = input[idx : idx + 3]
        button_a_x, button_a_y = map(lambda x: int(x), re.findall(r"\d+", block[0].split(": ")[-1]))
        button_b_x, button_b_y = map(lambda x: int(x), re.findall(r"\d+", block[1].split(": ")[-1]))
        prize_x, prize_y = map(lambda x: int(x), re.findall(r"\d+", block[2].split(": ")[-1]))
        if part2:
            prize_x += 10000000000000
            prize_y += 10000000000000

        # Solve for:
        # a1 * x + b1 * y = c1
        # a2 * x + b2 * y = c2
        a_presses = (prize_x * button_b_y - prize_y * button_b_x) / (button_a_x * button_b_y - button_a_y * button_b_x)
        b_presses = (prize_y * button_a_x - prize_x * button_a_y) / (button_a_x * button_b_y - button_a_y * button_b_x)
        if a_presses == int(a_presses) and b_presses == int(b_presses):
            tokens += int(3 * a_presses + b_presses)

        idx += 4

    return tokens


if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read().split("\n")[:-1]

    print("Part 1:", solve(input))
    print("Part 2:", solve(input, part2=True))
