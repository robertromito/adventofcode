import string


def read_input(file):
    with open(file) as f:
        for line in f:
            pairing = line.strip().split(",")
            assert len(pairing) == 2, "bad pairing line assumption"
            yield pairing


def parse_elf_assignments(raw_elf_assignment: str) -> list:
    return [int(s) for s in raw_elf_assignment.split("-")]


def is_proper_subset(a: list, b: list) -> bool:
    return (a[0] <= b[0]) and (a[1] >= b[1])


def solve_problem(input_file) -> int:

    proper_subset_pairings = 0

    for pairing in read_input(input_file):
        a, b = parse_elf_assignments(pairing[0]), parse_elf_assignments(pairing[1])

        assert len(a) == 2, "bad first assignments"
        assert a[0] <= a[1], f"inverted first assignment, {a}"

        assert len(b) == 2, "bad second assignments"
        assert b[0] <= b[1], f"inverted second assignment: {b}"

        if is_proper_subset(a, b) or is_proper_subset(b, a):
            proper_subset_pairings += 1
            print(f"{proper_subset_pairings:4} {a} {b}")

    return proper_subset_pairings


print(f"== day 4 part 1 example", "=" * 40)
example_answer = solve_problem("input.example.txt")
assert example_answer == 2, f"calculated answer: {example_answer}"

print(f"== day 4 part 1 problem", "=" * 40)
final_answer = solve_problem("input.txt")

wrong_answers = [(569, "too high")]
for a in wrong_answers:
    assert final_answer != a[0], f"{a[0]} is wrong: {a[1]}"

print(f"final answer is: {final_answer}")
assert 542 == final_answer