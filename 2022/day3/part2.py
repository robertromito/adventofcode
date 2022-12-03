import string


def read_input(file):
    with open(file) as f:
        while True:
            group1 = f.readline()
            group2 = f.readline()
            group3 = f.readline()
            if not group3:
                break
            yield [group1.strip(), group2.strip(), group3.strip()]


def get_priority(rucksack_item: str) -> int:
    assert rucksack_item in string.ascii_letters
    return string.ascii_letters.index(rucksack_item) + 1


def get_badge_for_group(*elves: list[str]) -> str:
    assert len(elves) == 3
    return set(elves[0]).intersection(*elves[1:]).pop()


def solve_problem(input_file) -> int:

    priorities = 0

    for elf1, elf2, elf3 in read_input(input_file):
        badge = get_badge_for_group(elf1, elf2, elf3)
        badge_priority = get_priority(badge)
        priorities += badge_priority

    return priorities


print(f"== day 3 part 2 ", "=" * 40)
example_answer = solve_problem("input.example.txt")
assert example_answer == 70, f"calculated answer: {example_answer}"

final_answer = solve_problem("input.txt")

wrong_answers = [(7484, "too low")]
for a in wrong_answers:
    assert final_answer != a[0], f"{a[0]} is wrong: {a[1]}"

print(f"final answer is: {final_answer}")
assert final_answer == 2425
