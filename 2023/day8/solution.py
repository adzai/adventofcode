from math import lcm


def step(instruction, nodes, current_node):
    if instruction == "L":
        return nodes[current_node][0]
    else:
        return nodes[current_node][1]


def part1(instructions, nodes):
    steps = 0
    current_node = "AAA"
    while current_node != "ZZZ":
        current_node = step(instructions[steps % len(instructions)], nodes, current_node)
        steps += 1

    print("Part 1:", steps)


def part2(instructions, nodes, current_nodes):
    steps = 0
    found_node_exits_to_num_of_steps = {}
    while True:
        for i, current_node in enumerate(current_nodes):
            next_node = step(instructions[steps % len(instructions)], nodes, current_node)
            current_nodes[i] = next_node

        for current_node in current_nodes:
            if current_node[-1] == "Z" and not found_node_exits_to_num_of_steps.get(current_node):
                found_node_exits_to_num_of_steps[current_node] = steps + 1

        steps += 1

        if len(found_node_exits_to_num_of_steps.keys()) == len(current_nodes):
            break

    print("Part 2:", lcm(*found_node_exits_to_num_of_steps.values()))


if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read().split("\n")[:-1]

    instructions = input[0]

    nodes = {}
    part2_starting_nodes = []
    for line in input[2:]:
        node, left_right = line.split(" = ")
        nodes[node] = tuple(left_right[1:-1].split(", "))
        if node[-1] == "A":
            part2_starting_nodes.append(node)

    part1(instructions, nodes)
    part2(instructions, nodes, part2_starting_nodes)
