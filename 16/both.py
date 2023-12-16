def step(pos: tuple[int, int], delta: tuple[int, int]) -> tuple[int, int]:
    return pos[0] + delta[0], pos[1] + delta[1]


def next(char: str, delta: tuple[int, int]) -> list[tuple[int, int]]:
    match char:
        case ".":
            return [delta]
        case "\\":
            return [(delta[1], delta[0])]
        case "/":
            return [(-delta[1], -delta[0])]
        case "|":
            if delta[1] == 0:
                return [delta]
            return [(1, 0), (-1, 0)]
        case "-":
            if delta[0] == 0:
                return [delta]
            return [(0, 1), (0, -1)]

    raise Exception()


def in_bounds(grid: list[str], pos: tuple[int, int]) -> bool:
    return 0 <= pos[0] < len(grid) and 0 <= pos[1] < len(grid[0])


def num_energised(grid: list[str], start_pos, start_delta) -> int:
    energized = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

    processing_queue: list[tuple[tuple[int, int], tuple[int, int]]] = [
        (start_pos, start_delta)
    ]

    visited = {}
    while len(processing_queue) > 0:
        pos, delta = processing_queue.pop(0)

        while (pos, delta) not in visited and in_bounds(grid, pos):
            row, col = pos
            energized[row][col] = True

            visited[(pos, delta)] = True

            deltas = next(grid[row][col], delta)

            if len(deltas) == 2:
                processing_queue.append((step(pos, deltas[1]), deltas[1]))

            delta = deltas[0]
            pos = step(pos, delta)

    return sum(
        energized[i][j] for j in range(len(energized[0])) for i in range(len(energized))
    )


with open("in.txt") as file:
    grid = file.read().split("\n")

total_p1 = num_energised(grid, (0, 0), (0, 1))

print("Part 1", total_p1)

total_p2 = 0

col_len = len(grid)
for i in range(col_len):
    from_right = num_energised(grid, (i, 0), (0, 1))
    from_left = num_energised(grid, (i, col_len - 1), (0, -1))
    total_p2 = max(total_p2, from_right, from_left)

row_len = len(grid[0])
for i in range(row_len):
    from_above = num_energised(grid, (0, i), (1, 0))
    from_below = num_energised(grid, (row_len - 1, i), (-1, 0))
    total_p2 = max(total_p2, from_above, from_below)

print("Part 2", total_p2)
