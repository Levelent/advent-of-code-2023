def is_valid_reflection(grid: list[list[str]], index: int) -> bool:
    i = index
    j = index + 1
    while i >= 0 and j < len(grid):
        if grid[i] != grid[j]:
            return False
        i -= 1
        j += 1
    return True


with open("in.txt") as file:
    sections = file.read().split("\n\n")

total = 0
for section in sections:
    grid = [list(line) for line in section.split("\n")]

    for i in range(len(grid) - 1):
        if is_valid_reflection(grid, i):
            total += 100 * (i + 1)
    
    grid_t = [[grid[i][j] for i in range(len(grid))] for j in range(len(grid[0]))]

    for i in range(len(grid_t) - 1):
        if is_valid_reflection(grid_t, i):
            total += i + 1

print(total)