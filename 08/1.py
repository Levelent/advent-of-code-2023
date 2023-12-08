class Node:
    def __init__(self, name) -> None:
        self.name = name
        self.left = None
        self.right = None
    
    def set(self, left, right) -> None:
        self.left = left
        self.right = right
    
    def __repr__(self) -> str:
        return f"{self.name} = ({self.left.name}, {self.right.name})"

with open("in.txt") as file:
    instructions, node_text = file.read().split("\n\n")

node_info = node_text.replace("=", ",").replace("(", "").replace(")", "").replace(",", "").split("\n")
node_info = [n.split() for n in node_info]

nodes = {n[0]: Node(n[0]) for n in node_info}

for n in node_info:
    nodes[n[0]].set(nodes[n[1]], nodes[n[2]])

print(nodes)

instr_size = len(instructions)

curr_node = nodes["AAA"]
steps = 0
while curr_node.name != "ZZZ":
    match instructions[steps % instr_size]:
        case "L":
            curr_node = curr_node.left
        case "R":
            curr_node = curr_node.right
    steps += 1

print(steps)