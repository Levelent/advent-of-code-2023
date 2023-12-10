from enum import Enum, auto


class Direction(Enum):
    LEFT = auto()
    RIGHT = auto()
    UP = auto()
    DOWN = auto()

    def apply_direction(self, i: int, j: int) -> (int, int):
        match self:
            case Direction.RIGHT:
                return i, j + 1
            case Direction.LEFT:
                return i, j - 1
            case Direction.DOWN:
                return i + 1, j
            case Direction.UP:
                return i - 1, j
        return i, j

    def opposite(self):
        match self:
            case Direction.RIGHT:
                return Direction.LEFT
            case Direction.LEFT:
                return Direction.RIGHT
            case Direction.DOWN:
                return Direction.UP
            case Direction.UP:
                return Direction.DOWN


char_to_direction_set = {
    "-": [Direction.LEFT, Direction.RIGHT],
    "|": [Direction.UP, Direction.DOWN],
    "┌": [Direction.RIGHT, Direction.DOWN],
    "┐": [Direction.LEFT, Direction.DOWN],
    "┘": [Direction.LEFT, Direction.UP],
    "└": [Direction.RIGHT, Direction.UP],
    ".": [],
}


def find_start(lines):
    for i in range(len(lines)):
        j = lines[i].find("S")
        if j != -1:
            return i, j
    return -1, -1


def replace_start(x, y):
    # replace S with correct pipe
    start_directions = []
    if lines[x][y - 1] in ["-", "└", "┌"]:
        start_directions.append(Direction.LEFT)
    if lines[x][y + 1] in ["-", "┐", "┘"]:
        start_directions.append(Direction.RIGHT)
    if lines[x + 1][y] in ["|", "┘", "└"]:
        start_directions.append(Direction.DOWN)
    if lines[x - 1][y] in ["|", "┌", "┐"]:
        start_directions.append(Direction.UP)

    # reverse dictionary lookup
    for key, val in char_to_direction_set.items():
        if start_directions == val:
            lines[x] = lines[x].replace("S", key)


with open("in.txt") as file:
    text = file.read()

# replace with nicer printing characters
for before, after in [("F", "┌"), ("7", "┐"), ("L", "└"), ("J", "┘")]:
    text = text.replace(before, after)

lines = text.split("\n")

marked = [["." for _ in range(len(lines[0]))] for _ in range(len(lines))]

# find and replace S with the correct pipe
x, y = find_start(lines)
replace_start(x, y)

marked[x][y] = lines[x][y]
prev_dir = char_to_direction_set[lines[x][y]][0]
i, j = prev_dir.apply_direction(x, y)

# extract and mark remaining loop
path_length = 1
while i != x or j != y:
    poss = char_to_direction_set[lines[i][j]]

    # go in the unexplored direction
    if poss[0] != prev_dir.opposite():
        next_dir = poss[0]
    else:
        next_dir = poss[1]

    marked[i][j] = lines[i][j]
    i, j = next_dir.apply_direction(i, j)

    prev_dir = next_dir
    path_length += 1


# use non-zero rule to count cells inside the main loop
total_inside = 0
for i in range(len(lines)):
    is_inside = False
    num_inside_line = 0
    for j in range(len(lines[0])):
        if marked[i][j] != ".":
            if Direction.DOWN in char_to_direction_set[lines[i][j]]:
                is_inside = not is_inside
        elif is_inside:
            num_inside_line += 1
            marked[i][j] = "*"

    print("".join(marked[i]), num_inside_line)

    total_inside += num_inside_line

print(f"Part 1: {path_length // 2} | Part 2: {total_inside}")
