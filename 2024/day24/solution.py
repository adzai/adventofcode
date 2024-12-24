def is_x_y_combination(lhs, rhs):
    return lhs.startswith("x") and rhs.startswith("y") or lhs.startswith("y") and rhs.startswith("x")

def get_output(wires):
    output = ""
    for wire, val in sorted(wires.items()):
        if wire.startswith("z"):
            output += str(val)

    return output[::-1]

def part1(wires, instructions):
    processed = set()
    total_num_of_wires = set()
    ordered = []
    for line in instructions:
        inp, out = line.split(" -> ")
        lhs, op, rhs = inp.split(" ")
        total_num_of_wires.add(lhs)
        total_num_of_wires.add(rhs)
        total_num_of_wires.add(out)
    while len(wires.keys()) < len(total_num_of_wires):
        for line in instructions:
            inp, out = line.split(" -> ")
            lhs, op, rhs = inp.split(" ")
            if wires.get(lhs) is None or wires.get(rhs) is None or (lhs, rhs, out) in processed:
                continue

            match op:
                case "XOR":
                    wires[out] = wires[lhs] ^ wires[rhs]
                case "OR":
                    wires[out] = wires[lhs] or wires[rhs]
                case "AND":
                    wires[out] = wires[lhs] and wires[rhs]

            ordered.append((lhs, rhs, out))
            processed.add((lhs, rhs, out))

    return int(get_output(wires), 2)

def part2(instructions):
    faulty, should_be_ors = [], []
    for line in instructions:
        inp, out = line.split(" -> ")
        lhs, op, rhs = inp.split(" ")
        if op == "AND" and lhs != "x00" and rhs != "x00":
            should_be_ors.append(out)
        if not is_x_y_combination(lhs, rhs) and op == "XOR" and not out.startswith("z"):
            faulty.append(out)
        if out.startswith("z") and out != "z45" and op != "XOR":
            faulty.append(out)

    for line in instructions:
        inp, out = line.split(" -> ")
        lhs, op, rhs = inp.split(" ")
        if op == "OR" and lhs not in should_be_ors:
            faulty.append(lhs)
        elif op == "OR" and rhs not in should_be_ors:
            faulty.append(rhs)
        elif op == "XOR" and lhs in should_be_ors:
            faulty.append(lhs) 
        elif op == "XOR" and rhs in should_be_ors:
            faulty.append(rhs)

    return ",".join(sorted(list(set(faulty))))

if __name__ == "__main__":
    wires = {}
    with open("input.txt") as f:
        input_data = f.read().split("\n\n")

        for dat in input_data[0].split("\n"):
            wire, num = dat.split(": ")
            wires[wire] = int(num)

        instructions = input_data[1].split("\n")[:-1]


    print("Part 1:", part1(wires, instructions))
    print("Part 2:", part2(instructions))
