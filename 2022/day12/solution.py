with open("12.txt") as f:
    input = f.read().split("\n")[:-1]


class Vertex:
    def __init__(self, col, row, letter):
        self.col = col
        self.row = row
        self.letter = letter
        self.neighbors = []
        self.cost = float("inf")


class Graph:
    def __init__(self, lines, reverse_order=False):
        self._reverse_order = reverse_order
        self.vertices = self._get_vertices(lines)
        self.edges = self._populate_neighbors(lines)

    def _get_vertices(self, lines):
        all_vertices = []
        for col, line in enumerate(lines):
            for row, letter in enumerate(line):
                all_vertices.append(Vertex(col, row, letter))

        return all_vertices

    def _add_neighbor_if_qualifies(self, vertex, potential_neighbor):
        if self._reverse_order:
            cond = self._get_ascii_val(potential_neighbor.letter) - self._get_ascii_val(vertex.letter) >= -1
        else:
            cond = self._get_ascii_val(vertex.letter) - self._get_ascii_val(potential_neighbor.letter) >= -1
        if cond:
            vertex.neighbors.append(potential_neighbor)

    def _populate_neighbors(self, lines):
        row_bound = len(lines[0])
        col_bound = len(lines)
        for vertex in self.vertices:
            if vertex.col - 1 >= 0:
                potential_neighbor = self.vertices[(vertex.col - 1) * row_bound + vertex.row]
                self._add_neighbor_if_qualifies(vertex, potential_neighbor)
            if vertex.col + 1 < col_bound:
                potential_neighbor = self.vertices[(vertex.col + 1) * row_bound + vertex.row]
                self._add_neighbor_if_qualifies(vertex, potential_neighbor)
            if vertex.row - 1 >= 0:
                potential_neighbor = self.vertices[vertex.col * row_bound + (vertex.row - 1)]
                self._add_neighbor_if_qualifies(vertex, potential_neighbor)
            if vertex.row + 1 < row_bound:
                potential_neighbor = self.vertices[vertex.col * row_bound + (vertex.row + 1)]
                self._add_neighbor_if_qualifies(vertex, potential_neighbor)

    def _get_ascii_val(self, letter):
        if letter == "S":
            return ord("a")
        if letter == "E":
            return ord("z")

        return ord(letter)


def get_bfs_cost(start, end):
    q = [start]
    explored = []
    while q:
        current_vertex = q.pop(0)
        if current_vertex.letter in end:
            return current_vertex.cost
        for neighbor in current_vertex.neighbors:
            neighbor.cost = min(current_vertex.cost + 1, neighbor.cost)
            if neighbor not in explored:
                explored.append(neighbor)
                q.append(neighbor)

    return float("inf")  # Didn't find path


def part1(lines):
    graph = Graph(lines, reverse_order=False)
    for vertex in graph.vertices:
        if vertex.letter == "S":
            vertex.cost = 0
            print("Part 1:", get_bfs_cost(vertex, end="E"))
            return


def part2(lines):
    graph = Graph(lines, reverse_order=True)
    for vertex in graph.vertices:
        if vertex.letter == "E":
            vertex.cost = 0
            print("Part 2:", get_bfs_cost(vertex, end="Sa"))
            return


part1(input)
part2(input)
