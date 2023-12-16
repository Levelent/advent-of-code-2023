def rotate_90(grid: list[list]) -> list[list]:
    return [list(line[::-1]) for line in zip(*grid)]


def sum_frequencies(grid: list[list[str]]) -> int:
    total = 0
    for i in range(len(grid)):
        point_value = len(grid) - i
        num_rocks = sum(c == "O" for c in grid[i])
        total += point_value * num_rocks
    return total


def tilt_across_rows(row: list[str]) -> list[str]:
    new_row: list[str] = []

    last_hash = -1
    rock_buffer = 0
    for i in range(len(row)):
        match row[i]:
            case "#":
                new_row = (
                    new_row[: last_hash + 1]
                    + (["O"] * rock_buffer)
                    + new_row[last_hash + 1 :]
                )
                rock_buffer = 0
                new_row.append("#")
                last_hash = i
            case ".":
                new_row.append(".")
            case "O":
                rock_buffer += 1
    return new_row


with open("in.txt") as file:
    grid = [list(line) for line in file.read().split("\n")]


curr_grid = rotate_90(rotate_90(rotate_90(grid)))

part1_grid = [tilt_across_rows(row + ["#"])[:-1] for row in curr_grid]
print("Part 1:", sum_frequencies(rotate_90(part1_grid)))

grid_history = []
while curr_grid not in grid_history:
    grid_history.append(curr_grid)
    # complete a cycle
    for i in range(4):
        curr_grid = [tilt_across_rows(row + ["#"])[:-1] for row in curr_grid]
        curr_grid = rotate_90(curr_grid)

# stop when we reach the first repeated grid - all future grids will repeat in a cycle
# figure out which of these grids in the cycle will be the 1 billionth

found_at = grid_history.index(curr_grid)
cycle_length = len(grid_history) - found_at

target_offset = 1_000_000_000 % cycle_length
found_offset = found_at % cycle_length

offset_diff = target_offset - found_offset
if offset_diff < 0:  # non-negative offset
    offset_diff += cycle_length

final_grid = grid_history[found_at + offset_diff]

print("Part 2:", sum_frequencies(rotate_90(final_grid)))
