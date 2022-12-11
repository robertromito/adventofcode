from dataclasses import dataclass, field

DAY = 10
PART = 1

KEY_CYCLES = [20, 60, 100, 140, 180, 220]


@dataclass
class Clock:
    ticks: int = 0
    reg_x: int = 1
    key_signal_strength: list = field(default_factory=list)

    def cycle(self):
        while True:
            self.ticks += 1
            if self.ticks in KEY_CYCLES:
                self.key_signal_strength.append(self.ticks * self.reg_x)

            yield self

            if self.ticks == KEY_CYCLES[-1]:
                return

    def addx(self, value: int):
        self.reg_x += value

    def __repr__(self):
        return f"[ticks: {self.ticks:3}] register: {self.reg_x:3}"


@dataclass
class Instruction:
    cmd: str
    cycles: int = 0

    def execute(self, clock: Clock):
        self.cycles += 1

        if self.cmd == "noop":
            return True

        if self.cmd.startswith("addx"):
            _, value = self.cmd.split()
            if self.cycles == 2:
                clock.addx(int(value))
                return True

        return False

    def __repr__(self) -> str:
        return f"instruction: {self.cmd}"


def solve_problem(input_file: str) -> int:

    with open(input_file) as f:
        instructions = [i.strip() for i in f.readlines()]

    instruction_count = 0
    i = Instruction(instructions[instruction_count])

    clock = Clock()
    for tick in clock.cycle():
        # print(f"{tick} -> {i}")
        if i.execute(tick):
            instruction_count += 1
            i = Instruction(instructions[instruction_count])
        pass

    return sum(clock.key_signal_strength)


print(f"== day {DAY} part {PART} example", "=" * 40)
example_answer = solve_problem("input.example.txt")
assert example_answer == 13140, f"calculated answer: {example_answer}"
print(f"example answer is: {example_answer}")


print(f"== day {DAY} part {PART} problem", "=" * 40)
final_answer = solve_problem("input.txt")

wrong_answers = []
for a in wrong_answers:
    assert final_answer != a[0], f"{a[0]} is wrong: {a[1]}"

print(f"final answer is: {final_answer}")
assert 16060 == final_answer
