letter_to_pos = {"x": 0, "m": 1, "a": 2, "s": 3}

class Rule():
    def __init__(self, pos: int, is_greater: bool, number: int, outcome: str) -> None:
        self.pos = pos
        self.is_greater = is_greater
        self.number = number
        self.outcome = outcome
    
    def is_applied(self, part: list[int]) -> bool:
        part_num = part[self.pos]
        if self.is_greater:
            return part_num > self.number
        else:
            return part_num < self.number
    
    def __repr__(self) -> str:
        return f"{'xmas'[self.pos]}{'>' if self.is_greater else '<'}{self.number}:{self.outcome}"
        

class Workflow():
    def __init__(self, rules: list[Rule], end: str) -> None:
        self.rules = rules
        self.end = end
    
    def __repr__(self) -> str:
        return f"{self.rules} ~ {self.end}"
    
    def apply(self, part: list[int]):
        for rule in self.rules:
            if rule.is_applied(part):
                return rule.outcome
        return self.end


with open("in.txt") as file:
    section_a, section_b = file.read().split("\n\n")

# parse workflows
workflows: dict[str, Workflow] = {}

for line in section_a.split("\n"):
    name, rest = line[:-1].split("{")
    instrs = rest.split(",")
    last = instrs[-1]
    rules = []
    for instr in instrs[:-1]:
        condition, outcome = instr.split(":")
        pos = letter_to_pos[condition[0]]
        is_greater = condition[1] == ">"
        number = int(condition[2:])
        rules.append(Rule(pos, is_greater, number, outcome))
    workflows[name] = Workflow(rules, last)

# parse instructions, and apply workflow to each
total = 0
for line in section_b.split("\n"):
    part = [int(text[2:]) for text in line[1:-1].split(",")]
    workflow_name = "in"
    while workflow_name not in ["A", "R"]:
        workflow_name = workflows[workflow_name].apply(part)
    
    if workflow_name == "A":
        total += sum(part)

print(total)