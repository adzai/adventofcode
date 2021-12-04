with open("aoc18-input.txt") as f:
    lines = f.readlines()


def custom_eval(chars, left_precedence=True):
    i = 0
    chars = chars.split(" ")
    chosen_chars = ["*", "+"] if left_precedence else ["+"]
    while False not in [x in chars for x in chosen_chars]:
        i = i % len(chars)
        if chars[i] in chosen_chars:
            chars = chars[:i-1] + \
                [str(eval("".join(chars[i-1:i+2])))] + chars[i+2:]
            i = -1
        i += 1
    return eval("".join(chars))


def evaluate(chars, left_precedence=True):
    paren = chars.find("(")
    while paren != -1:
        chars = chars[:paren] + evaluate(chars[paren+1:],
                                         left_precedence=left_precedence)
        paren = chars.find("(")
    closing_paren = chars.find(")")
    if closing_paren != -1:
        return str(custom_eval
                   (chars[:closing_paren], left_precedence=left_precedence)) + \
            chars[closing_paren+1:]
    else:
        return custom_eval(chars, left_precedence=left_precedence)


def print_results(lines):
    sums1, sums2 = 0, 0
    for line in lines:
        res1 = evaluate(line)
        res2 = evaluate(line, left_precedence=False)
        sums1 += res1
        sums2 += res2
    print("Part 1:", sums1)
    print("Part 2:", sums2)


print_results(lines)
