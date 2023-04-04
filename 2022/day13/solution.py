from functools import cmp_to_key

with open("13.txt") as f:
    pairs = f.read().split("\n\n")
    pairs[-1] = pairs[-1][:-1]


def ensure_list(val):
    return val if isinstance(val, list) else [val]


def pair_iter(first, second):
    if not first:
        return True
    if not second:
        return False
    for x, y in zip(first, second):
        if type(x) != type(y):
            x = pair_iter(ensure_list(x), ensure_list(y))
            if x is None:
                continue
            else:
                return x
        if isinstance(x, list):
            x = pair_iter(x, y)
            if x is None:
                continue
            else:
                return x
        if x == y:
            continue
        return x < y

    if len(first) != len(second):
        return len(first) < len(second)


def part1(pairs):
    right_order_indices = []
    for i, pair in enumerate(pairs):
        first, second = pair.split("\n")
        first = eval(first)
        second = eval(second)
        if pair_iter(first, second):
            right_order_indices.append(i + 1)

    print("Part 1:", sum(right_order_indices))


def part2(pairs):
    def pair_iter_wrapper(x, y):
        res = pair_iter(x, y)
        if res:
            return -1
        return 1

    new_pairs = []
    for pair in pairs:
        first, second = pair.split("\n")
        new_pairs.append(eval(first))
        new_pairs.append(eval(second))

    new_pairs.append([[2]])
    new_pairs.append([[6]])
    new = sorted(new_pairs, key=cmp_to_key(pair_iter_wrapper))

    divider_packets_indices = []
    for i, elem in enumerate(new):
        if elem == [[2]] or elem == [[6]]:
            divider_packets_indices.append(i + 1)

    print("Part 2:", divider_packets_indices[0] * divider_packets_indices[1])


part1(pairs)
part2(pairs)
