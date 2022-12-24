with open("input.txt") as f:
    input = f.read().strip()

# input = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"


def solve(input, offset):
    chars = input[: offset - 1]
    for i, char in enumerate(input[offset - 1:]):
        chars += char
        if len(set(chars)) == offset:
            return i + offset
        else:
            chars = chars[1:]


print("Part 1:", solve(input, 4))
print("Part 2:", solve(input, 14))
