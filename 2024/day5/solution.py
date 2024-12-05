class Node:
    def __init__(self, val):
        self.val = val
        self.edges = []

    def __repr__(self):
        return f"Node({self.val})"


def get_instructions_and_pages(input):
    collecting_instructions = True
    instructions, pages = [], []
    for line in input:
        if line == "":
            collecting_instructions = False
            continue

        if collecting_instructions:
            instructions.append(line)
        else:
            pages.append(line)

    return instructions, pages


def get_parsed_nodes():
    graph_nodes = {}
    for instruction in instructions:
        left, right = instruction.split("|")
        node = Node(left)
        if graph_nodes.get(left) is None:
            graph_nodes[left] = node

        graph_nodes[left].edges.append(right)

    return graph_nodes


def correct_invalid_page_numbers(page_numbers, graph_nodes):
    seen_numbers = set()
    idx = 0
    while idx < len(page_numbers):
        number = page_numbers[idx]
        node = graph_nodes.get(number)
        if node is None:
            seen_numbers.add(number)
            idx += 1
            continue

        seen_edges = set()
        for edge in node.edges:
            if edge in seen_numbers:
                seen_edges.add(edge)

        seen_numbers.add(number)
        if seen_edges:
            for i, edge in enumerate(page_numbers):
                if edge in seen_edges:
                    page_numbers.remove(number)
                    page_numbers = page_numbers[:i] + [number] + page_numbers[i:]
                    break
        idx += 1

    return page_numbers


def is_page_correct(page_numbers, graph_nodes):
    seen_numbers = set()
    for number in page_numbers:
        node = graph_nodes.get(number)
        if node is None:
            seen_numbers.add(number)
            continue

        for edge in node.edges:
            if edge in seen_numbers:
                return False

        seen_numbers.add(number)

    return True


if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read().split("\n")[:-1]

    instructions, pages = get_instructions_and_pages(input)
    graph_nodes = get_parsed_nodes()

    correct_lines, incorrect_lines = [], []
    for page in pages:
        page = page.split(",")
        if is_page_correct(page, graph_nodes):
            correct_lines.append(page)
        else:
            incorrect_lines.append(page)

    part1_total = 0
    for line in correct_lines:
        part1_total += int(line[len(line) // 2])

    print("Part 1:", sum([int(line[len(line) // 2]) for line in correct_lines]))

    part2_total = 0
    for line in [correct_invalid_page_numbers(incorrect_line, graph_nodes) for incorrect_line in incorrect_lines]:
        part2_total += int(line[len(line) // 2])
    print("Part 2:", part2_total)
