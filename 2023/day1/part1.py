DAY = 1
PART = 1


def read_input(file):
    with open(file) as f:
        return f.readlines()


def solve_problem(input_file):
    calibration_total = 0
    for l in read_input(input_file):
        calibration_line_values = [c for c in l if c.isdigit()]
        calibration_value = f"{calibration_line_values[0]}{calibration_line_values[-1]}"
        calibration_total += int(calibration_value)
    return calibration_total


print(f"== day {DAY} part {PART} example", "=" * 40)
example_answer = solve_problem("input.example.txt")
print(f"example answer is: {example_answer}")
assert example_answer == 142, f"calculated answer: {example_answer}"

final_answer = solve_problem("input.txt")
print(f"final answer is: {final_answer}")
assert final_answer == 54630
