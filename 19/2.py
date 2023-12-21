import math

letter_to_pos = {"x": 0, "m": 1, "a": 2, "s": 3}

class Rule():
    def __init__(self, pos: int, is_greater: bool, number: int, outcome: str) -> None:
        self.pos = pos
        self.is_greater = is_greater
        self.number = number
        self.outcome = outcome
    
    def split_ranges(self, rating_ranges: list[tuple[int, int]]) -> tuple[list[tuple[int, int]], list[tuple[int, int]]]:
        rating_lower, rating_upper = rating_ranges[self.pos]

        if rating_upper < rating_lower:
            raise Exception("oh dear")
        
        true_ranges = [rating_range for rating_range in rating_ranges]
        false_ranges = [rating_range for rating_range in rating_ranges]

        if self.is_greater: # cut out bottom part of range
            true_ranges[self.pos] = self.number + 1, rating_upper
            false_ranges[self.pos] = rating_lower, self.number
        else:  # cut out top part of range
            true_ranges[self.pos] = rating_lower, self.number - 1
            false_ranges[self.pos] = self.number, rating_upper
        
        return true_ranges, false_ranges
    
    def __repr__(self) -> str:
        return f"{'xmas'[self.pos]}{'>' if self.is_greater else '<'}{self.number}:{self.outcome}"

def is_valid_range(range: tuple[int, int]):
    return range[0] <= range[1]

def num_in_ranges(ranges: list[tuple[int, int]]):
    return math.prod([b - a + 1 for a, b in ranges])


class Workflow():
    def __init__(self, rules: list[Rule], end: str) -> None:
        self.rules = rules
        self.end = end
    
    def __repr__(self) -> str:
        return f"{self.rules} ~ {self.end}"
    
    def total_accepted(self, part: list[tuple[int, int]]) -> int:
        total = 0
        this_part = part
        for rule in self.rules:
            true_ranges, false_ranges = rule.split_ranges(this_part)

            if is_valid_range(true_ranges[rule.pos]):
                if rule.outcome == "A":
                    total += num_in_ranges(true_ranges)
                elif rule.outcome != "R":
                    total += workflows[rule.outcome].total_accepted(true_ranges)
                        
            
            if not is_valid_range(false_ranges[rule.pos]):
                return total
            
            this_part = false_ranges
        
        if self.end == "A":
            total += num_in_ranges(this_part)
        elif self.end != "R":
            total += workflows[self.end].total_accepted(this_part)

        return total


with open("in.txt") as file:
    section_a = file.read().split("\n\n")[0]

# parse workflows
workflows: dict[str, Workflow] = {}

for line in section_a.split("\n"):
    name, rest = line[:-1].split("{")
    instrs = rest.split(",")
    last = instrs[-1]
    rules = []
    for instr in instrs[:-1]:
        # print(instr)
        condition, outcome = instr.split(":")
        pos = letter_to_pos[condition[0]]
        is_greater = condition[1] == ">"
        num = int(condition[2:])
        rules.append(Rule(pos, is_greater, num, outcome))
    workflows[name] = Workflow(rules, last)

part_ranges: list[tuple[int, int]] = [(1, 4000), (1, 4000), (1, 4000), (1, 4000)]

print(workflows["in"].total_accepted(part_ranges))