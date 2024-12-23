from collections import defaultdict


def part1(graph):
    total, three_connected_nodes = 0, []
    for node, neighbors in graph.items():
        interconnected = set()
        for i in range(len(neighbors)):
            for j in range(len(neighbors)):
                if i == j:
                    continue

                if neighbors[i] in graph[neighbors[j]]:
                    connected_nodes = tuple(sorted((node, neighbors[i], neighbors[j])))
                    interconnected.add(connected_nodes)

        if interconnected not in three_connected_nodes:
            three_connected_nodes.extend(interconnected)

    for nodes in list(set(three_connected_nodes)):
        for node in nodes:
            if node.startswith("t"):
                total += 1
                break

    return total


# https://en.wikipedia.org/wiki/Bron%E2%80%93Kerbosch_algorithm
def part2(r, p, x, graph):
    if len(p) == 0 and len(x) == 0:
        return [r]

    cliques = []
    for node in p.union(set([])):
        cliques.extend(part2(r.union(set([node])), p.intersection(graph[node]), x.intersection(graph[node]), graph))
        p.remove(node)
        x.add(node)

    return cliques


if __name__ == "__main__":
    with open("input.txt") as f:
        input_data = f.read().split("\n")[:-1]

    graph = defaultdict(list)
    for data in input_data:
        left, right = data.split("-")
        graph[left].append(right)
        graph[right].append(left)

    print("Part 1:", part1(graph))
    print(
        "Part 2:",
        ",".join(
            sorted(sorted(part2(set([]), set(graph.keys()), set([]), graph), key=lambda x: len(x), reverse=True)[0])
        ),
    )
