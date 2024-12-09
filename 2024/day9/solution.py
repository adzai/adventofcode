def get_block(input):
    block = []
    id = 0
    for i, char_to_move in enumerate(input):
        if i % 2 == 0:
            block.extend([str(id)] * int(char_to_move))
            id += 1
        else:
            block.extend("." * int(char_to_move))

    return block

def get_checksum(block):
    return sum((i * int(char) for i, char in enumerate(block) if char != "."))


def part1(block):
    empty_spaces = [i for i in range(len(block)) if block[i] == "."]
    idx = len(block) - 1
    while idx > empty_spaces[0]:
        char_to_move = block[idx]
        if char_to_move == ".":
            idx -= 1
            continue
        space = empty_spaces.pop(0)
        block[space] = char_to_move
        block[idx] = "."
        idx -= 1

    return get_checksum(block)


def part2(block):
    in_span = False
    empty_space_spans = []
    start_idx = 0
    for i in range(len(block)):
        if block[i] == ".":
            if not in_span:
                in_span = True
                start_idx = i
        else:
            if in_span:
                empty_space_spans.append((start_idx, i))
                in_span = False

    idx = len(block) - 1
    while idx > empty_space_spans[0][0]:
        if block[idx] == ".":
            idx -= 1
            continue

        chars_to_move = [block[idx]]
        while block[idx - 1] == chars_to_move[0]:
            chars_to_move.append(block[idx - 1])
            idx -= 1

        num_of_chars_to_move = len(chars_to_move)

        for i, span in enumerate(empty_space_spans):
            if span[1] > idx:
                break

            if (span_diff := span[1] - span[0]) >= num_of_chars_to_move:
                for j in range(span[0], span[0] + num_of_chars_to_move):
                    block[j] = chars_to_move[0]

                if num_of_chars_to_move == span_diff:
                    empty_space_spans.pop(i)
                else:
                    empty_space_spans[i] = (empty_space_spans[i][0] + num_of_chars_to_move, empty_space_spans[i][1])

                for i in range(idx, idx + num_of_chars_to_move):
                    block[i] = "."

                break

        idx -= 1

    return get_checksum(block)


if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read().strip()

    print("Part 1:", part1(get_block(input)))
    print("Part 2:", part2(get_block(input)))
