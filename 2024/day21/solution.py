import re
from functools import lru_cache


class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.edges = []


class Edge:
    def __init__(self, node: Node, val) -> None:
        self.node = node
        self.val = val


class Graph:
    def __init__(self) -> None:
        self.nodes = {}

    def insert(self, node: Node):
        self.nodes[node.val] = node

    def add_edges(self, node_val, other_node_val, left_to_right_val, right_to_left_val):
        node, other_node = self.nodes[node_val], self.nodes[other_node_val]

        edge = Edge(other_node, left_to_right_val)
        node.edges.append(edge)

        edge = Edge(node, right_to_left_val)
        other_node.edges.append(edge)


def get_numeric_graph():
    graph = Graph()
    for val in "A0123456789":
        graph.insert(Node(val))

    graph.add_edges("0", "A", ">", "<")
    graph.add_edges("0", "2", "^", "v")
    graph.add_edges("A", "3", "^", "v")
    graph.add_edges("1", "2", ">", "<")
    graph.add_edges("1", "4", "^", "v")
    graph.add_edges("2", "3", ">", "<")
    graph.add_edges("2", "5", "^", "v")
    graph.add_edges("3", "6", "^", "v")
    graph.add_edges("4", "5", ">", "<")
    graph.add_edges("4", "7", "^", "v")
    graph.add_edges("5", "6", ">", "<")
    graph.add_edges("5", "8", "^", "v")
    graph.add_edges("6", "9", "^", "v")
    graph.add_edges("7", "8", ">", "<")
    graph.add_edges("8", "9", ">", "<")

    return graph


def get_directional_graph():
    graph = Graph()
    for val in "A<^>v":
        graph.insert(Node(val))

    graph.add_edges("<", "v", ">", "<")
    graph.add_edges("v", ">", ">", "<")
    graph.add_edges("v", "^", "^", "v")
    graph.add_edges(">", "A", "^", "v")
    graph.add_edges("^", "A", ">", "<")

    return graph


@lru_cache(maxsize=None)
def find_all_paths_to_key(graph, starting_val, destination_val):
    starting_node = graph.nodes[starting_val]
    queue = [(0, starting_node, "")]
    final_instructions, shortest, visited = [], None, set()
    while len(queue) > 0:
        cost, current_node, instructions = queue.pop(0)

        if current_node.val == destination_val:
            shortest = cost
            final_instructions.append(instructions + "A")
            continue

        if (shortest is not None and cost > shortest) or current_node.val in visited:
            continue

        visited.add((current_node.val, instructions))

        for edge in current_node.edges:
            new_cost = cost + 2 if len(instructions) > 0 and edge.val != instructions[-1] else cost + 1
            queue.append((new_cost, edge.node, instructions + edge.val))

    return final_instructions


@lru_cache(maxsize=None)
def get_minimal_amount_of_key_presses(graph, code, max_depth, current_depth=0):
    if current_depth == max_depth:
        return len(code)

    current_position, num_of_key_presses = "A", 0
    for key in code:
        seq1 = find_all_paths_to_key(graph, current_position, key)
        num_of_key_presses += min(
            get_minimal_amount_of_key_presses(directional_graph, sequence, max_depth, current_depth + 1)
            for sequence in seq1
        )

        current_position = key

    return num_of_key_presses


def solve(codes, num_of_robots):
    total = 0
    for code in codes:
        last_instructions = get_minimal_amount_of_key_presses(numeric_graph, code, num_of_robots + 1)
        code_num = int("".join(re.findall(r"\d+", code)))
        total += last_instructions * code_num

    return total


if __name__ == "__main__":
    with open("input.txt") as f:
        codes = f.read().split("\n")[:-1]

    numeric_graph = get_numeric_graph()
    directional_graph = get_directional_graph()

    print("Part 1:", solve(codes, num_of_robots=2))
    print("Part 2:", solve(codes, num_of_robots=25))
