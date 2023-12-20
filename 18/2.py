direction_map = [(1, 0), (0, 1), (-1, 0), (0, -1)]

with open("in.txt") as file:
    instructions = [line.split()[2] for line in file.read().split("\n")]

# shoelace algorithm my beloved
    
last_x, last_y = (0, 0)

area = 0
total_steps = 0
for hex_code in instructions:
    dx, dy = direction_map[int(hex_code[-2])]
    
    steps = int(hex_code[2:-2], 16)
    total_steps += steps

    this_x, this_y = last_x + dx * steps, last_y + dy * steps

    area += last_x * this_y - this_x * last_y

    last_x, last_y = this_x, this_y

# every new hash, add 1/2. At the end, add 1 (for the additional 1/4 from each clockwise turn)
total = (area + total_steps) // 2 + 1
print(total)

# 