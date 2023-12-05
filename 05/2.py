class Range:
    def __init__(self, lower: int, upper: int) -> None:
        self.lower = lower
        self.upper = upper

    def __repr__(self) -> str:
        return f"[{self.lower} to {self.upper}]"


class Mapping:
    def __init__(self, dest: int, source: int, length: int) -> None:
        self.lower = source
        self.upper = source + length - 1
        self.shift = dest - source


def get_mapping(mappings: list[Mapping], curr_range: Range) -> list[Range]:
    ranges = []
    working_range = curr_range
    for mapping in mappings:
        # check if the ranges overlap
        a = max(mapping.lower, working_range.lower)
        b = min(mapping.upper, working_range.upper)
        if a <= b:
            ranges.append(Range(a + mapping.shift, b + mapping.shift))

            # unmapped range below is identity mapped
            if working_range.lower < a:
                ranges.append(Range(working_range.lower, a - 1))

            # consider only range above going forward
            if working_range.upper <= b:
                return ranges
            working_range = Range(b + 1, working_range.upper)

    # identity map leftover range
    ranges.append(working_range)
    return ranges


with open("in.txt") as file:
    sections = file.read().split("\n\n")

# set up seed ranges
first_line = sections[0].split()[1:]
pairs = zip(first_line[::2], first_line[1::2])
current_ranges = [
    Range(int(start), int(start) + int(length) - 1) for start, length in pairs
]

sections = sections[1:]

for section in sections:
    # set up mapping objects
    mappings = [
        Mapping(*[int(num) for num in triple.split()])
        for triple in section.split("\n")[1:]
    ]
    mappings.sort(key=lambda c: c.lower)

    new_ranges: list[Range] = []
    for curr_range in current_ranges:
        new_ranges.extend(get_mapping(mappings, curr_range))

    # if input even larger, can merge overlapping ranges after each map
    current_ranges = new_ranges

# lowest value across all ranges
print(min(current_ranges, key=lambda r: r.lower).lower)
