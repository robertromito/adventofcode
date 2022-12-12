import math
import operator
import time

DAY = 11
PART = 2

OPS = {
    "*": operator.mul,
    "+": operator.add,
}


class Monkey:
    def __init__(self, definition) -> None:
        self.definition = definition
        self.number = definition[0].split()[1].rstrip(":")
        self.items = [int(i) for i in definition[1].split(":")[1].split(",")]

        _, operator, operand = definition[2].split("=")[1].split()
        if operand == "old":
            self.op = lambda x,_: x*x
            self.operand = ""
        else:
            self.operand = int(operand)
            self.op = OPS[operator]

        self.test_divisor = int(definition[3].split()[-1])
        self.true_monkey = int(definition[4].split()[-1])
        self.false_monkey = int(definition[5].split()[-1])

        self.items_inspected = 0

    def take_turn1(self, monkeys, mysterious_division_factor):
        for i in self.items:
            self.items_inspected += 1
            worry_level = self.op(i, self.operand) % mysterious_division_factor
            pass_to_monkey = (
                self.true_monkey
                if (worry_level % self.test_divisor) == 0
                else self.false_monkey
            )
            monkeys[pass_to_monkey].items.append(worry_level)
        self.items = []


    def take_turn2(self, monkeys, mysterious_division_factor):
        self.items_inspected += len(self.items)

        worry_items = [
            self.op(i, self.operand) % mysterious_division_factor for i in self.items
        ]

        monkeys[self.true_monkey].items.extend(
            [i for i in worry_items if (i % self.test_divisor) == 0]
        )

        monkeys[self.false_monkey].items.extend(
            [i for i in worry_items if (i % self.test_divisor) != 0]
        )

        self.items = []

    def take_turn(self, monkeys, mysterious_division_factor):
        self.take_turn1(monkeys, mysterious_division_factor)


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
    
    # Help!
    # https://www.reddit.com/r/adventofcode/comments/zifqmh/comment/izv2oxh/?utm_source=reddit&utm_medium=web2x&context=3
    # https://www.reddit.com/r/adventofcode/comments/zifqmh/comment/izuzwjl/?utm_source=reddit&utm_medium=web2x&context=3
    mysterious_division_factor = math.prod([m.test_divisor for m in monkeys])

    rounds_to_play = 10000

    print("Let's play monkey business!")
    for i in range(rounds_to_play):
        print(f"\r> round {i + 1} [{time.process_time():5.5f} seconds]", end="", flush=True)
        if i + 1 in [1, 20, 1000]:
            print()
        for m in monkeys:
            m.take_turn(monkeys, mysterious_division_factor)
            if i + 1 in [1, 20, 1000]:
                print(m)

    
    print()
    for m in monkeys:
        print(m)

    ranked_monkey_business = sorted([i.items_inspected for i in monkeys], reverse=True)

    print(ranked_monkey_business)

    return ranked_monkey_business[0] * ranked_monkey_business[1]


print(f"== day {DAY} part {PART} example", "=" * 40)
example_answer = solve_problem("input.example.txt")
assert example_answer == 2713310158, f"calculated answer: {example_answer}"
print(f"example answer is: {example_answer}")


print(f"== day {DAY} part {PART} problem", "=" * 40)
final_answer = solve_problem("input.txt")

wrong_answers = []
for a in wrong_answers:
    assert final_answer != a[0], f"{a[0]} is wrong: {a[1]}"

print(f"final answer is: {final_answer}")
assert 23612457316 == final_answer
