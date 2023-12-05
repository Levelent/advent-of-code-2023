def get_mapping(conditions: list[(int, int, int)], value: int) -> int:
    for dest, source, length in conditions:
        if source <= value < source + length:
            return value + (dest - source)
    return value


with open("in.txt") as file:
    sections = file.read().split("\n\n")

current_vals = [int(num) for num in sections[0].split()[1:]]
maps = sections[1:]

for map in maps:
    conditions = [
        [int(num) for num in triple.split()] for triple in map.split("\n")[1:]
    ]
    current_vals = [get_mapping(conditions, val) for val in current_vals]

print(min(current_vals))
