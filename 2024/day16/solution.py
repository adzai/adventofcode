from collections import defaultdict
from queue import PriorityQueue

DIRECTIONS = (-1, 0), (1, 0), (0, -1), (0, 1)
STARTING_DIRECTION_IDX = 3


def solve(
    grid: dict[tuple[int, int], str], starting_tile: tuple[int, int], ending_tile: tuple[int, int]
) -> tuple[int, int]:
    priority_queue = PriorityQueue()
    priority_queue.put(
        (0, (starting_tile[0], starting_tile[1], STARTING_DIRECTION_IDX), [(starting_tile[0], starting_tile[1])])
    )
    tile_to_score = defaultdict(lambda: float("inf"))
    final_scores_to_paths = defaultdict(list)
    while not priority_queue.empty():
        current_score, current_tile_with_direction, path = priority_queue.get()
        current_tile_x, current_tile_y, current_direction_idx = current_tile_with_direction
        if (current_tile_x, current_tile_y) == ending_tile:
            final_scores_to_paths[current_score].extend(
                path + [(current_tile_with_direction[0], current_tile_with_direction[1])]
            )

        for new_direction_idx, new_direction in enumerate(DIRECTIONS):
            new_tile_with_direction = (
                current_tile_x + new_direction[0],
                current_tile_y + new_direction[1],
                new_direction_idx,
            )
            if (
                grid_val := grid.get((new_tile_with_direction[0], new_tile_with_direction[1]))
            ) is not None and grid_val != "#":
                new_score = current_score + (1001 if new_direction_idx != current_direction_idx else 1)
                if new_score <= tile_to_score[new_tile_with_direction]:
                    tile_to_score[new_tile_with_direction] = new_score
                    priority_queue.put(
                        (
                            new_score,
                            (
                                new_tile_with_direction[0],
                                new_tile_with_direction[1],
                                new_tile_with_direction[2],
                            ),
                            path + [(current_tile_with_direction[0], current_tile_with_direction[1])],
                        )
                    )

    lowest_score = min(final_scores_to_paths.keys())

    return lowest_score, len(set(final_scores_to_paths[lowest_score]))


if __name__ == "__main__":
    with open("input.txt") as f:
        input_data = f.read().split("\n")[:-1]

    matrix = [list(row) for row in input_data]
    grid = {(x, y): cell for x, row in enumerate(input_data) for y, cell in enumerate(list(row))}

    starting_tile, ending_tile = None, None
    for coordinates, cell in grid.items():
        if cell == "S":
            starting_tile = coordinates
        elif cell == "E":
            ending_tile = coordinates

    assert starting_tile is not None
    assert ending_tile is not None

    lowest_score, number_of_tiles_on_best_paths = solve(grid, starting_tile, ending_tile)
    print("Part 1:", lowest_score)
    print("Part 2:", number_of_tiles_on_best_paths)
