num_cards = int(input())

total = 0
for _ in range(num_cards):
    line = input()
    
    # Strip card number
    line = line[line.find(":")+1:]
    left, right = line.split("|")
    winning = set(int(text) for text in left.strip().split())
    numbers = set(int(text) for text in right.strip().split())
    num_common = len(numbers.intersection(winning))
    if num_common > 0:
        total += 2 ** (num_common - 1)


print(total)