# observations on input:
# grid dimensions are 131 x 131
# steps is 26591365, divided by 131 is 202300 rem 65
# 65 * 2 + 1 = 131

x = 26501365
y = 131

a, b = divmod(x, y)
print(a, b)

with open("in.txt") as file:
    lines = file.read().split("\n")
print(lines)

start_row, start_col = -1, -1
for row in range(len(lines)):
    col = lines[row].find("S")
    if col != -1:
        start_row, start_col = row, col
        break

grid = [list(line) for line in lines]

grid[start_row][start_col] = "O"

n_steps = 65

# run bfs
frontier: set[tuple[int, int]] = set([(start_row, start_col)])
for i in range(n_steps):
    print(i + 1, len(frontier), frontier)
    next_frontier = set()

    for row, col in frontier:
        for i, j in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            if grid[row + i][col + j] == ".":
                next_frontier.add((row + i, col + j))

    frontier = next_frontier
    for row, col in frontier:
        grid[row][col] = "O"

[print("".join(line)) for line in grid]

total = 0
# count based on diagonal offset - even number of steps
is_offset = start_row % 2 != start_col % 2
for row in range(len(grid)):
    total += sum(c == "O" for c in grid[row][is_offset + (row % 2) :: 2])
print(total)
