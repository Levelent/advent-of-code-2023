import math

class Node:
    def __init__(self, value: int) -> None:
        self.value: int = value
        self.adjacent: list["Node"] = []
        self.visited: bool = False
        self.distance = math.inf
    
    def __repr__(self) -> str:
        return f"{self.value} ({self.distance}) -> {[adj.value for adj in self.adjacent]}"

with open("in.txt") as file:
    grid = file.read().split("\n")

# node_layers[row][col][direction][layer]
node_layers = [[[[Node(int(grid[i][j])) for j in range(len(grid[0]))] for i in range(len(grid))] for _ in range(3)] for _ in range(2)]

# add connections to the next layer
for depth in range(2):
    for i in range(len(grid)):
        for j in range(len(grid[0]) - 1):
            node_layers[0][depth][i][j].adjacent.append(node_layers[0][depth+1][i][j+1])
            node_layers[0][depth][i][j+1].adjacent.append(node_layers[0][depth+1][i][j])
    
    for i in range(len(grid) - 1):
        for j in range(len(grid[0])):
            node_layers[1][depth][i][j].adjacent.append(node_layers[1][depth+1][i+1][j])
            node_layers[1][depth][i+1][j].adjacent.append(node_layers[1][depth+1][i][j])

for depth in range(3):
    for i in range(len(grid)):
        for j in range(len(grid[0]) - 1):
            node_layers[1][depth][i][j].adjacent.append(node_layers[0][0][i][j+1])
            node_layers[1][depth][i][j+1].adjacent.append(node_layers[0][0][i][j])
    
    for i in range(len(grid) - 1):
        for j in range(len(grid[0])):
            node_layers[0][depth][i][j].adjacent.append(node_layers[1][0][i+1][j])
            node_layers[0][depth][i+1][j].adjacent.append(node_layers[1][0][i][j])

# run dijkstra's algorithm on the transformed node set
starting = Node(0)
starting.adjacent.append(node_layers[0][0][0][1])
starting.adjacent.append(node_layers[1][0][1][0])
starting.distance = 0

curr = starting
unvisited = set()

while curr != None:
    curr.visited = True
    for adj in curr.adjacent:
        new_dist = curr.distance + adj.value
        adj.distance = min(adj.distance, new_dist)
        if not adj.visited:
            unvisited.add(adj)

    curr = min(unvisited, default=None, key=lambda n: n.distance)
    if curr != None:
        unvisited.remove(curr)

final_nodes = [node_layers[direction][depth][len(grid)-1][len(grid[0])-1] for depth in range(3) for direction in range(2)]

print(min(final_nodes, key=lambda n: n.distance).distance)
