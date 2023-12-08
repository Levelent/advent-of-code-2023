class Flaggable:
    def __init__(self, thing) -> None:
        self.thing = thing
        self.flag = False

    def __repr__(self) -> str:
        return str(self.thing)

def is_digit(char: str) -> bool:
    return 48 <= ord(char) <= 57

if __name__ == "__main__":
    num_lines = int(input())

    grid = []
    possible_parts = []

    # First pass, get into grid
    for _ in range(num_lines):
        line = input()
        row = []
        num_length = 0

        for i in range(len(line)):
            if is_digit(line[i]):
                num_length += 1
                if i == len(line) - 1 or not is_digit(line[i + 1]):
                    part = Flaggable(int(line[i - num_length + 1 : i + 1]))
                    possible_parts.append(part)
                    for _ in range(num_length):
                        row.append(part)
                    num_length = 0
            else:
                if line[i] != ".":
                    row.append(Flaggable(-1))
                else:
                    row.append(None)
                num_length = 0

        grid.append(row)

    # Second pass (flag objects)
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] != None and grid[row][col].thing == -1:
                for a in range(-1, 2):
                    for b in range(-1, 2):
                        if (
                            (a != 0 or b != 0)
                            and 0 <= row + a <= len(grid)
                            and 0 <= col + b <= len(grid[0])
                            and grid[row + a][col + b] != None
                        ):
                            grid[row + a][col + b].flag = True

    total = sum([part.thing for part in possible_parts if part.flag])
    print(total)
