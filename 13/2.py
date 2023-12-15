def is_valid_smudge_reflection(grid: list[list[str]], index: int) -> bool:
    has_smudged = False
    i = index
    j = index + 1
    while i >= 0 and j < len(grid):
        if grid[i] != grid[j]:
            if has_smudged:
                return False
            
            # can we change 1 symbol to have them match?
            num_same = sum(a == b for a, b in zip(grid[i], grid[j]))
            if num_same != len(grid[i]) - 1:
                return False
            
            has_smudged = True

        i -= 1
        j += 1
    
    return has_smudged


with open("in.txt") as file:
    sections = file.read().split("\n\n")

total = 0
for section in sections:
    grid = [list(line) for line in section.split("\n")]

    for i in range(len(grid) - 1):
        if is_valid_smudge_reflection(grid, i):
            total += 100 * (i + 1)
    
    grid_t = [[grid[i][j] for i in range(len(grid))] for j in range(len(grid[0]))]

    for i in range(len(grid_t) - 1):
        if is_valid_smudge_reflection(grid_t, i):
            total += i + 1

print(total)