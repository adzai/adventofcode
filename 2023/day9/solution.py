def get_line_sub_sequences(line):
    line_to_diff = line
    all_sub_sequences = []
    while True:
        new_seq = []
        for i, val in enumerate(line_to_diff[:-1]):
            new_seq.append(line_to_diff[i + 1] - val)

        all_sub_sequences.append(new_seq)

        if not any(new_seq):
            return all_sub_sequences

        line_to_diff = new_seq


def extrapolate_part1(extrapolation_seq, i):
    extrapolation_seq[i + 1].append(extrapolation_seq[i][-1] + extrapolation_seq[i + 1][-1])


def extrapolate_part2(extrapolation_seq, i):
    extrapolation_seq[i + 1].insert(0, extrapolation_seq[i + 1][0] - extrapolation_seq[i][0])


def solve(lines, extrapolation_func, total_idx):
    total = 0
    for line in lines:
        sub_sequences = get_line_sub_sequences(line)
        extrapolation_seq = sub_sequences[::-1]
        extrapolation_seq.append(line)
        for i, _ in enumerate(extrapolation_seq[:-1]):
            extrapolation_func(extrapolation_seq, i)

        total += extrapolation_seq[-1][total_idx]

    return total


if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read().split("\n")[:-1]

    lines = []
    for line in input:
        lines.append([int(x) for x in line.split()])

    print("Part 1:", solve(lines, extrapolate_part1, -1))
    print("Part 2:", solve(lines, extrapolate_part2, 0))
