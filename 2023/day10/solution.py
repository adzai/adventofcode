import time
import shapely


class Node:
    def __init__(self, val, valid_indexes, coords):
        self.children = []
        self.valid_indexes = valid_indexes
        self.val = val
        self.coords = coords
        self.cost = float("inf") if val != "S" else 0
        self.visited = False

    def __repr__(self):
        return f"{self.val}, cost: {self.cost} POS:{self.coords}, children:{[child.val for child in self.children]}"


def bfs(root, i):
    nodes_to_visit = [root.children[i]]
    cost = 1
    visited = set([root.coords])
    while nodes_to_visit:
        node = nodes_to_visit.pop(0)
        if node.coords in visited:
            continue
        visited.add(node.coords)
        node.cost = min(cost, node.cost)
        for child in node.children:
            if child.coords not in visited:
                nodes_to_visit.append(child)
        cost += 1


def construct_graph(input):
    pipe_to_valid_connections = {
        "|": ((-1, 0), (1, 0)),
        "-": ((0, -1), (0, 1)),
        "L": ((-1, 0), (0, 1)),
        "J": ((-1, 0), (0, -1)),
        "7": ((1, 0), (0, -1)),
        "F": ((1, 0), (0, 1)),
        "S": ((-1, 0), (1, 0), (0, -1), (0, 1)),
    }
    nodes = {}
    root = None
    for col_idx, col_val in enumerate(input):
        for row_idx, row_val in enumerate(col_val):
            if row_val != ".":
                nodes[(col_idx, row_idx)] = Node(row_val, pipe_to_valid_connections[row_val], (col_idx, row_idx))

            if row_val == "S":
                root = nodes[(col_idx, row_idx)]

    assert root is not None

    for node_positions, node in nodes.items():
        for pos in node.valid_indexes:
            col = node_positions[0] + pos[0]
            row = node_positions[1] + pos[1]
            try:
                if other_node := nodes.get((col, row)):
                    node.children.append(other_node)
            except IndexError as e:
                print(e)
                pass

    return nodes, root


def part1(nodes, root):
    maxes = []
    for i in range(len(root.children)):
        bfs(root, i)
        maxes.append(max([node.cost for node in nodes.values() if node.cost != float("inf")]))

    print("Part 1:", min(maxes))


if __name__ == "__main__":
    with open("input.txt") as f:
        input = f.read().split("\n")[:-1]

    nodes, root = construct_graph(input)
    part1(nodes, root)
