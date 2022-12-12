from dataclasses import dataclass, field

DAY = 11
PART = 1


class Monkey:
    def __init__(self, definition) -> None:
        self.definition = definition
        self.number = definition[0].split()[1].rstrip(":")
        self.items = [int(i) for i in definition[1].split(":")[1].split(",")]
        self.operation = definition[2].split("=")[-1].strip()
        self.test_divisor = int(definition[3].split()[-1])
        self.true_monkey = int(definition[4].split()[-1])
        self.false_monkey = int(definition[5].split()[-1])

        self.items_inspected = 0

    def take_turn(self, monkeys):
        while len(self.items):
            self.items_inspected += 1
            old = self.items.pop(0)
            worry_level = eval(self.operation) // 3
            pass_to_monkey = (
                self.true_monkey
                if (worry_level % self.test_divisor) == 0
                else self.false_monkey
            )
            monkeys[pass_to_monkey].items.append(worry_level)

    def __repr__(self) -> str:
        return "".join(
            (f"Monkey {self.number} ", f"inspected {self.items_inspected:5} items")
        )


def solve_problem(input_file: str) -> int:

    monkeys = []

    with open(input_file) as f:
        monkey_def = None
        for l in [l.strip() for l in f.readlines()]:
            if not l:
                assert len(monkey_def) == 6, f"invalid monkey def: {monkey_def}"
                monkeys.append(Monkey(monkey_def))
            elif l.startswith("Monkey "):
                monkey_def = [l]
            else:
                monkey_def.append(l)
        monkeys.append(Monkey(monkey_def))

    assert len(monkeys) > 0, "Did not find any monkeys"

    rounds_to_play = 20

    for _ in range(rounds_to_play):
        for m in monkeys:
            m.take_turn(monkeys)
            # print(m)

    ranked_monkey_business = sorted([i.items_inspected for i in monkeys], reverse=True)

    return ranked_monkey_business[0] * ranked_monkey_business[1]


print(f"== day {DAY} part {PART} example", "=" * 40)
example_answer = solve_problem("input.example.txt")
assert example_answer == 10605, f"calculated answer: {example_answer}"
print(f"example answer is: {example_answer}")


print(f"== day {DAY} part {PART} problem", "=" * 40)
final_answer = solve_problem("input.txt")

wrong_answers = []
for a in wrong_answers:
    assert final_answer != a[0], f"{a[0]} is wrong: {a[1]}"

print(f"final answer is: {final_answer}")
assert 110264 == final_answer
