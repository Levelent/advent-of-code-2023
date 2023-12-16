def hash_alg(string: str) -> int:
    curr_val = 0
    for c in string:
        curr_val = ((curr_val + ord(c)) * 17) % 256
    return curr_val


with open("in.txt") as file:
    strings = file.read().split(",")

total = sum(hash_alg(string) for string in strings)
print(total)
