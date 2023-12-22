class Pulse():
    def __init__(self, sender: str, receiver: str, is_high: bool) -> None:
        self.sender = sender
        self.receiver = receiver
        self.is_high = is_high

    def __repr__(self) -> str:
        return f"({self.sender}, {self.receiver}, {self.is_high})"

class Module():
    def __init__(self, name, dest_names: list[str]) -> None:
        self.name = name
        self.destinations = dest_names

    def receive(self, _: Pulse) -> bool | None:
        pass

    def __repr__(self) -> str:
        return f"{self.name}: {self.destinations}"

class FlipFlop(Module):
    def __init__(self, name, dest_names) -> None:
        super().__init__(name, dest_names)
        self.is_on = False
    
    def receive(self, pulse: Pulse) -> bool | None:
        if pulse.is_high:
            return None
        self.is_on = not self.is_on
        return self.is_on
    
    def __repr__(self) -> str:
        return f"%{super().__repr__()} - {self.is_on}"

class Conjunction(Module):
    def __init__(self, name, dest_names) -> None:
        super().__init__(name, dest_names)
        self.last_recieved = {}
    
    def receive(self, pulse: Pulse) -> bool | None:
        self.last_recieved[pulse.sender] = pulse.is_high

        for val in self.last_recieved.values():
            if not val:
                return True
        return False
    
    def __repr__(self) -> str:
        return f"&{super().__repr__()} - {self.last_recieved}"

with open("in.txt") as file:
    lines = [line.split(" -> ") for line in file.read().split("\n")]

pulse_queue: list[Pulse] = []
modules: dict[str, Module] = {}
conjunctions = []

for module_text, dests_text in lines:
    dests = [d for d in dests_text.split(", ")]
    if module_text == "broadcaster":
        pulse_queue = [Pulse(module_text, d, False) for d in dests]
        continue

    module_type = module_text[0]
    module_name = module_text[1:]
    if module_type == "%":
        modules[module_name] = FlipFlop(module_name, dests)
    else:  # module_type == "&"

        modules[module_name] = Conjunction(module_name, dests)
        conjunctions.append(modules[module_name])

for conj in conjunctions:
    for val in modules.values():
        if conj.name in val.destinations:
            conj.last_recieved[val.name] = False

iterations = 10000
pulses_sent: list[int] = [(len(pulse_queue) + 1) * iterations, 0]

# secretly dfs

for i in range(iterations):
    if i % 10000 == 0:
        print(i)
    this_pulse_queue = [p for p in pulse_queue]

    while len(this_pulse_queue) != 0:
        this_pulse, this_pulse_queue = this_pulse_queue[0], this_pulse_queue[1:]
        # print(this_pulse, this_pulse_queue) 
        if this_pulse.receiver in ["xl", "ln", "xp", "gp"]:
            if not this_pulse.is_high:
                print(this_pulse.receiver, i+1)
            continue
        receiver_module = modules[this_pulse.receiver]
        new_pulse_state = receiver_module.receive(this_pulse)
        if new_pulse_state != None:
            pulses_sent[new_pulse_state] += len(receiver_module.destinations)
            this_pulse_queue.extend([Pulse(receiver_module.name, d, new_pulse_state) for d in receiver_module.destinations])

# print(modules)
# print(pulses_sent)
# print(pulses_sent[0] * pulses_sent[1])
print(3833 * 4021 * 4051 * 4057)