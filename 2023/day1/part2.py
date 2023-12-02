DAY = 1
PART = 2

import re


def read_input(file):
    with open(file) as f:
        return f.readlines()


def solve_problem(input_file):

    numbers_map = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }

    p = re.compile(f"({'|'.join(numbers_map.keys())}|[0-9])")

    calibration_total = 0

    for l in read_input(input_file):
        first_digit = ""
        last_digit = ""

        matches = [m for m in p.finditer(l.rstrip())]

        first_digit_raw = matches[0].group(0)
        first_digit = numbers_map.get(first_digit_raw, first_digit_raw)

        last_digit_raw = matches[-1].group(0)
        last_digit = numbers_map.get(last_digit_raw, last_digit_raw)

        calibration_value = f"{first_digit}{last_digit}"
        assert len(calibration_value) == 2

        calibration_total += int(calibration_value)

        print(
            f"{l.rstrip()} | {' '.join([m.group(0) for m in matches])} | {calibration_value} | {calibration_total}"
        )

    return calibration_total


print(f"== day {DAY} part {PART} example", "=" * 40)
example_answer = solve_problem("input.example.part2.txt")
print(f"example answer is: {example_answer}")
assert example_answer == 281, f"calculated answer: {example_answer}"

print(f"== day {DAY} part {PART} answer", "=" * 40)
final_answer = solve_problem("input.txt")
print(f"final answer is: {final_answer}")
assert final_answer < 54780, f"calculated answer: {final_answer} is too high"
assert final_answer > 54491, f"calculated answer: {final_answer} is too low"
