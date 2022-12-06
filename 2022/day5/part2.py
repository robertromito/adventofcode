import string

from collections import namedtuple

DAY = 5
PART = 2


def read_stacks(file):
    with open(file) as f:
        return f.readlines()


def get_starting_stacks(raw_stacks: list) -> list[list]:

    CHARS_PER_STACK_ITEM = 3

    raw_stacks.reverse()

    assert raw_stacks, "raw_stacks is empty or None"

    the_stacks: list = []

    number_of_stacks = int(max(raw_stacks[0].split()))
    assert number_of_stacks > 0, "no stacks found"

    for _ in range(number_of_stacks):
        the_stacks.append([])
    assert len(the_stacks) == number_of_stacks
    print(f"{number_of_stacks} stacks")

    chars_per_stack_line = (number_of_stacks * CHARS_PER_STACK_ITEM) + (
        number_of_stacks - 1
    )

    for raw in raw_stacks[1:]:
        items = raw.strip("\n")
        assert len(items) == chars_per_stack_line, "stack line not expected length"

        current_item_position = 0
        current_stack = 0
        while current_item_position < chars_per_stack_line:
            item = items[
                current_item_position : current_item_position + CHARS_PER_STACK_ITEM
            ]
            print(f"{items} {current_item_position:2} {item} to stack {current_stack:2}")
            if item.strip():
                assert len(item) == CHARS_PER_STACK_ITEM, "bad stack item length"
                the_stacks[current_stack].append(item[1])
            current_item_position += CHARS_PER_STACK_ITEM + 1
            current_stack += 1

    return the_stacks


def read_moves(file):
    with open(file) as f:
        for line in f:
            yield line.strip()


StackMove = namedtuple("StackMove", ["item_count", "from_stack", "to_stack"])


def solve_problem(stacks_file: str, moves_file: str) -> str:

    stacks = get_starting_stacks(read_stacks(stacks_file))
    for raw_move in read_moves(moves_file):
        assert raw_move.startswith("move "), "bad move line beginning"
        move_tokens =  raw_move.split()
        assert len(move_tokens) == 6, "move line doesn't have right number of tokens"
        move = StackMove(int(move_tokens[1]), int(move_tokens[3]), int(move_tokens[5]))
        # print(f"{stacks} : {move}")
        items_to_move:list = []
        for _ in range(move.item_count):
            items_to_move.insert(0, stacks[move.from_stack - 1].pop())
        stacks[move.to_stack - 1].extend(items_to_move)

    return "".join([s.pop() for s in stacks])


print(f"== day {DAY} part {PART} example", "=" * 40)
example_answer = solve_problem("stacks.example.txt", "moves.example.txt")
assert example_answer == "MCD", f"calculated answer: {example_answer}"

print(f"== day {DAY} part {PART} problem", "=" * 40)
final_answer = solve_problem("stacks.txt", "moves.txt")

wrong_answers = []
for a in wrong_answers:
    assert final_answer != a[0], f"{a[0]} is wrong: {a[1]}"

print(f"final answer is: {final_answer}")
assert "QRQFHFWCL" == final_answer