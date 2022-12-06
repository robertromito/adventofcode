from collections import deque

DAY = 6
PART = 1


def read_input(file) -> str:
    with open(file) as f:
        return f.read()


def solve_problem(input_file: str) -> int:

    signal = read_input(input_file)

    chars_read = 0
    last_four_chars = deque(maxlen=4)

    for s in signal:
        chars_read += 1
        last_four_chars.append(s)
        print(f"{chars_read} {s} {last_four_chars}")
        if len(set(last_four_chars)) == 4:
            break

    return chars_read


print(f"== day {DAY} part {PART} example", "=" * 40)
example_answer = solve_problem("input.example.txt")
assert example_answer == 7, f"calculated answer: {example_answer}"

print(f"== day {DAY} part {PART} problem", "=" * 40)
final_answer = solve_problem("input.txt")

wrong_answers = []
for a in wrong_answers:
    assert final_answer != a[0], f"{a[0]} is wrong: {a[1]}"

print(f"final answer is: {final_answer}")
assert 1929 == final_answer