import string


def read_input(file):
    with open(file) as f:
        return f.readlines()


def rucksack_compartments(rucksack: str) -> list[str]:
    rucksack_size = len(rucksack)
    assert rucksack_size % 2 == 0, f"rucksack is not even: {rucksack_size} [{rucksack}]"

    midpoint = rucksack_size // 2
    return rucksack[0:midpoint], rucksack[midpoint:]


def get_priority(rucksack_item: str) -> int:
    assert rucksack_item in string.ascii_letters
    return string.ascii_letters.index(rucksack_item) + 1


def solve_problem(input_file) -> int:

    priorities = 0

    for r in read_input(input_file):
        a, b = rucksack_compartments(r.strip())
        duplicates = set(a).intersection(b)
        if duplicates:
            duplicate_priority = sum([get_priority(i) for i in duplicates])
            priorities += duplicate_priority

    return priorities


print(f"== day 3 part 1 ", "=" * 40)
example_answer = solve_problem("input.example.txt")
assert example_answer == 157, f"calculated answer: {example_answer}"

final_answer = solve_problem("input.txt")

wrong_answers = [(7484, "too low")]
for a in wrong_answers:
    assert final_answer != a[0], f"{a[0]} is wrong: {a[1]}"

print(f"final answer is: {final_answer}")
