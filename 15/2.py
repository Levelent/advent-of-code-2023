def hash_alg(string: str) -> int:
    curr_val = 0
    for c in string:
        curr_val = ((curr_val + ord(c)) * 17) % 256
    return curr_val


box_map = {i: [] for i in range(256)}
text_to_focal_length_map = {}

with open("in.txt") as file:
    strings = file.read().split(",")

for string in strings:
    if string[-1] == "-":  # remove from box
        text = string[:-1]
        label = hash_alg(text)
        box = box_map[label]
        if text in box:
            box.remove(text)
            text_to_focal_length_map.pop(text)

    else:  # add to box (or update value)
        text, right = string.split("=")
        label = hash_alg(text)
        focal_length = int(right)

        if text not in box_map[label]:
            box_map[label].append(text)
        text_to_focal_length_map[text] = focal_length

# calculate sum of 'focusing power' on resulting items
total = 0
for text, focal_length in text_to_focal_length_map.items():
    label = hash_alg(text)
    idx = box_map[label].index(text)
    total += (label + 1) * (idx + 1) * focal_length

print(total)
