from functools import total_ordering
from enum import Enum


# Ascending value of hands
class HandType(Enum):
    HIGH_CARD = 1
    PAIR = 2
    TWO_PAIR = 3
    THREE_KIND = 4
    FULL_HOUSE = 5
    FOUR_KIND = 6
    FIVE_KIND = 7


def is_digit(char: str) -> bool:
    return 48 <= ord(char) <= 57


mappings = {"T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}


def get_strength(char: str):
    if is_digit(char):
        return int(char)
    return mappings[char]


@total_ordering
class Hand:
    def __init__(self, hand: str, bid: int) -> None:
        self.hand = hand
        self.hand_values = [get_strength(char) for char in hand]
        self.bid = bid
        self.hand_type = self.__find_hand_type()

    def __find_hand_type(self):
        # build dictionary of counts
        counts = {}
        for val in self.hand_values:
            if val in counts:
                counts[val] += 1
            else:
                counts[val] = 1

        # labels unimportant, only frequencies descending
        freqs = sorted(list(counts.values()), reverse=True)

        # determine hand type
        match freqs[0]:
            case 5:
                return HandType.FIVE_KIND
            case 4:
                return HandType.FOUR_KIND
            case 3:
                if freqs[1] == 2:
                    return HandType.FULL_HOUSE
                return HandType.THREE_KIND
            case 2:
                if freqs[1] == 2:
                    return HandType.TWO_PAIR
                return HandType.PAIR
        return HandType.HIGH_CARD

    def __eq__(self, other) -> bool:
        return self.hand_values == other.hand_values

    def __lt__(self, other) -> bool:
        # first compare hand type
        if self.hand_type.value != other.hand_type.value:
            return self.hand_type.value < other.hand_type.value

        # then compare individual cards in order
        for i in range(len(self.hand_values)):
            if self.hand_values[i] != other.hand_values[i]:
                return self.hand_values[i] < other.hand_values[i]

        return False

    def __repr__(self) -> str:
        return f"{self.hand} ({self.bid})"


with open("in.txt") as file:
    lines = [
        Hand(line.split()[0], int(line.split()[1])) for line in file.read().split("\n")
    ]

    # order by rank multiplier
    print(sum((i + 1) * hand.bid for i, hand in enumerate(sorted(lines))))
