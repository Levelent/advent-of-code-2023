class Node:
    def __init__(self, row, col) -> None:
        self.row = row
        self.col = col
        self.row_jumps = 0
        self.col_jumps = 0

    def __repr__(self) -> str:
        return f"({self.row+self.row_jumps}, {self.col+self.col_jumps})"


def node_dist(a: Node, b: Node, m: int) -> int:
    a_row = a.row + (m - 1) * a.row_jumps
    b_row = b.row + (m - 1) * b.row_jumps
    a_col = a.col + (m - 1) * a.col_jumps
    b_col = b.col + (m - 1) * b.col_jumps
    return abs(a_row - b_row) + abs(a_col - b_col)


with open("in.txt") as file:
    lines = file.read().split("\n")

nodes = [
    Node(row, col)
    for col in range(len(lines[0]))
    for row in range(len(lines))
    if lines[row][col] == "#"
]

by_row = sorted(nodes, key=lambda x: x.row)
by_col = sorted(nodes, key=lambda x: x.col)

# apply row jumps
total_row_jumps = 0
for idx, node in enumerate(by_row[:-1]):
    prev = by_row[idx]
    next = by_row[idx + 1]
    dist = next.row - prev.row
    if dist > 1:
        total_row_jumps += dist - 1
    next.row_jumps = total_row_jumps

# apply col jumps
total_col_jumps = 0
for idx, node in enumerate(by_col[:-1]):
    prev = by_col[idx]
    next = by_col[idx + 1]
    dist = next.col - prev.col
    if dist > 1:
        total_col_jumps += dist - 1
    next.col_jumps = total_col_jumps

# sum of distance between all pairs of points
total_dist_p1 = 0
total_dist_p2 = 0
for i in range(len(nodes)):
    for j in range(i + 1, len(nodes)):
        total_dist_p1 += node_dist(nodes[i], nodes[j], 2)
        total_dist_p2 += node_dist(nodes[i], nodes[j], 1000000)

print(total_dist_p1)
print(total_dist_p2)
