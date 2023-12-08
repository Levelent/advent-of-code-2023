num_cards = int(input())
card_quantities = [1 for _ in range(num_cards)]

total = 0
for i in range(num_cards):
    line = input()

    # Strip card number
    line = line[line.find(":") + 1 :]
    left, right = line.split("|")
    winning = set(int(text) for text in left.strip().split())
    numbers = set(int(text) for text in right.strip().split())
    num_common = len(numbers.intersection(winning))
    for j in range(num_common):
        card_quantities[i + 1 + j] += card_quantities[i]


print(sum(card_quantities))
