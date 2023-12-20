direction_map = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}

def move_and_mark(grid: list[list[str]], row: int, col: int, direction: str, steps: int) -> tuple[int, int]:
    
    d_row, d_col = direction_map[direction]

    for _ in range(steps):
        row += d_row
        col += d_col
        grid[row][col] = "#"
    return row, col

with open("in.txt") as file:
    instructions = [line.split() for line in file.read().split("\n")]

# pass 1, work out dimensions of grid
max_right = 0
min_right = 0
max_down = 0
min_down = 0
curr_right = 0
curr_down = 0
for direction, num_text, _ in instructions:
    num = int(num_text)
    match direction:
        case "U":
            curr_down -= num
            min_down = min(min_down, curr_down)
        case "D":
            curr_down += num
            max_down = max(max_down, curr_down)
        case "L":
            curr_right -= num
            min_right = min(min_right, curr_right)
        case "R":
            curr_right += num
            max_right = max(max_right, curr_right)

n_rows = max_down - min_down + 1
n_cols = max_right - min_right + 1

grid = [["." for _ in range(n_cols)] for _ in range(n_rows)]

# pass 2, actually mark locations on the grid

i = -min_down
j = -min_right
for direction, num_text, _ in instructions:
    i, j = move_and_mark(grid, i, j, direction, int(num_text))

# pass 3, similar algorithm to day 10 by checking square below for inside/outside toggle

count = 0
for row_idx in range(len(grid)):
    is_inside = False
    for col_idx in range(len(grid[0])):
        match grid[row_idx][col_idx]:
            case ".":
                if is_inside:
                    count += 1
                    grid[row_idx][col_idx] = "!"
            case "#":
                count += 1
                if row_idx+1 < n_rows and grid[row_idx+1][col_idx] == "#":
                    is_inside = not is_inside

print(count)
