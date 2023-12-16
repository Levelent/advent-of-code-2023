def step(delta: tuple[int, int], i: int, j: int) -> tuple[int, int]:
    return i + delta[0], j + delta[1]
    
def next(delta: tuple[int, int], char: str) -> list[tuple[int, int]]:
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


def in_bounds(grid: list[str], row: int, col: int) -> bool:
    return 0 <= row < len(grid) and 0 <= col < len(grid[0])


with open("in.txt") as file:
    grid = file.read().split("\n")


energized = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

processing_queue: list[tuple[int, int, tuple[int, int]]] = [(0, 0, (0, 1))]

visited = {}
while len(processing_queue) > 0:
    row, col, delta = processing_queue.pop(0)

    while (row, col, delta) not in visited and in_bounds(grid, row, col):
        visited[(row, col, delta)] = True

        energized[row][col] = True

        deltas = next(delta, grid[row][col])

        if len(deltas) == 2:
            row_split, col_split = step(deltas[1], row, col)
            processing_queue.append((row_split, col_split, deltas[1]))

        delta = deltas[0]
        row, col = step(delta, row, col)

# [print("".join(["#" if cell else "." for cell in row])) for row in energized]
total = sum(
    energized[i][j] for j in range(len(energized[0])) for i in range(len(energized))
)
print(total)
