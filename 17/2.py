from typing import Optional
import math

class Node:
    def __init__(self, value: int) -> None:
        self.value: int = value
        self.adjacent: list["Node"] = []
        self.visited: bool = False
        self.distance = math.inf
        self.is_last: bool = False
        self.parent: Optional[Node] = None
    
    def __repr__(self) -> str:
        return f"{self.value} -> {[adj.value for adj in self.adjacent]}"

with open("in.txt") as file:
    grid = file.read().split("\n")

# node_layers[row][col][direction][layer]
node_layers = [[[[Node(int(grid[i][j])) for _ in range(10)] for _ in range(4)] for j in range(len(grid[0]))] for i in range(len(grid))]

# when the direction doesn't change, increment the layer when moving
for depth in range(9):
    for i in range(len(grid)):
        for j in range(len(grid[0]) - 1):
            # left and right connections move up one layer
            node_layers[i][j][0][depth].adjacent.append(node_layers[i][j+1][0][depth+1])
            node_layers[i][j+1][2][depth].adjacent.append(node_layers[i][j][2][depth+1])
    
    for i in range(len(grid) - 1):
        for j in range(len(grid[0])):
            node_layers[i][j][1][depth].adjacent.append(node_layers[i+1][j][1][depth+1])
            node_layers[i+1][j][3][depth].adjacent.append(node_layers[i][j][3][depth+1])

# when the direction changes, reset the layer
for depth in range(3, 10):
    for i in range(len(grid)):
        for j in range(len(grid[0]) - 1):
            node_layers[i][j][1][depth].adjacent.append(node_layers[i][j+1][0][0])
            node_layers[i][j+1][1][depth].adjacent.append(node_layers[i][j][2][0])
            node_layers[i][j][3][depth].adjacent.append(node_layers[i][j+1][0][0])
            node_layers[i][j+1][3][depth].adjacent.append(node_layers[i][j][2][0])
    
    for i in range(len(grid) - 1):
        for j in range(len(grid[0])):
            node_layers[i][j][0][depth].adjacent.append(node_layers[i+1][j][1][0])
            node_layers[i+1][j][0][depth].adjacent.append(node_layers[i][j][3][0])
            node_layers[i][j][2][depth].adjacent.append(node_layers[i+1][j][1][0])
            node_layers[i+1][j][2][depth].adjacent.append(node_layers[i][j][3][0])

# determine which nodes the algorithm can stop at
final_grid = node_layers[len(grid)-1][len(grid[0])-1]
final_nodes = [final_grid[direction][depth] for depth in range(3, 10) for direction in range(4)]

for node in final_nodes:
    node.is_last = True

# run dijkstra's algorithm on the transformed node set
starting = Node(0)
starting.adjacent.append(node_layers[0][1][0][0])
starting.adjacent.append(node_layers[1][0][1][0])
starting.distance = 0

curr = starting
unvisited: set[Node] = set()

while curr != None and not curr.is_last:
    curr.visited = True
    for adj in curr.adjacent:
        if adj.visited:
            continue
        new_dist = curr.distance + adj.value
        if new_dist < adj.distance:
            adj.distance = new_dist
            adj.parent = curr
        unvisited.add(adj)

    curr = min(unvisited, default=None, key=lambda n: n.distance)
    if curr != None:
        unvisited.remove(curr)

lowest = min(final_nodes, key=lambda n: n.distance)

print(min(final_nodes, key=lambda n: n.distance).distance)
