from dataclasses import dataclass, field

DAY = 10
PART = 2


@dataclass
class Clock:
    ticks: int = 0
    reg_x: int = 1
    key_signal_strength: list = field(default_factory=list)

    def cycle(self):
        for t in range(240):
            self.ticks += 1
            yield self

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


class CRT:
    def __init__(self) -> None:
        self.sprite_location = [0, 1, 2]
        self.width = 40
        self.height = 6
        self.screen = []
        for _ in range(self.height):
            self.screen.append([" " for _ in range(self.width)])
        self.tick = 0

    def draw(self, clock: Clock):
        pixel = "."
        self.tick = clock.ticks - 1

        self.active_row = self.tick // self.width
        self.active_col = self.tick % self.width

        if self.active_col in self.sprite_location:
            pixel = "#"

        self.screen[self.active_row][self.active_col] = pixel

    def move_sprite(self, clock: Clock):
        new_sprint_center = (clock.reg_x) % self.width
        self.sprite_location = [
            new_sprint_center - 1,
            new_sprint_center,
            new_sprint_center + 1,
        ]

    def print(self, lines=6) -> None:
        print(
            "-" * 5,
            f"({self.active_row},{self.active_col}) {self.sprite_location} [{self.tick+1:3}]",
            "-" * 5,
        )
        for l in range(lines):
            print("".join(self.screen[l]).strip())


def solve_problem(input_file: str) -> CRT:

    with open(input_file) as f:
        instructions = [i.strip() for i in f.readlines()]

    instruction_count = 0
    instructions_total = len(instructions)
    i = Instruction(instructions[instruction_count])

    clock = Clock()
    crt = CRT()
    for tick in clock.cycle():
        crt.draw(tick)
        if (instruction_count < instructions_total) and i.execute(tick):
            crt.move_sprite(tick)
            instruction_count += 1
            if instruction_count < instructions_total:
                i = Instruction(instructions[instruction_count])
        # crt.print(lines=1)
    return crt


print(f"== day {DAY} part {PART} example", "=" * 40)
example = solve_problem("input.example.txt")
example.print()

expected_example_screen = [
    "##..##..##..##..##..##..##..##..##..##..",
    "###...###...###...###...###...###...###.",
    "####....####....####....####....####....",
    "#####.....#####.....#####.....#####.....",
    "######......######......######......####",
    "#######.......#######.......#######.....",
]

for i in range(len(expected_example_screen)):
    expected = expected_example_screen[i]
    actual = "".join(example.screen[i])
    assert expected == actual, f"screen line {i} is wrong:\ne {expected}\na {actual}"

print(f"== day {DAY} part {PART} problem", "=" * 40)
problem = solve_problem("input.txt")
problem.print() # answer is BACEKLHF
