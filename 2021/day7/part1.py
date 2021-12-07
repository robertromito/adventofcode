from datetime import datetime
from math import ceil
from statistics import median

DEBUG = True


def debug(msg, **kwargs):
    if DEBUG:
        print(msg, **kwargs)


def get_input(file):
    with open(file) as f:
        return f.readline()


def solve_problem(input_file):
    print(f"{input_file:-^40}")
    crab_positions = [int(f) for f in get_input(input_file).split(",")]
    max_dist = max(crab_positions) - min(crab_positions)
    median_dist = ceil(median(crab_positions))
    debug(f"{crab_positions} distances | " f"max: {max_dist} " f"median: {median_dist}")
    fuel_costs = [abs(c - median_dist) for c in crab_positions]
    answer = sum(fuel_costs)
    print(f"[{datetime.now()}] minimum amount of fuel required to align: {answer}")
    return answer


print("=" * 40)
example_answer = solve_problem("input.example.txt")
assert example_answer == 37, f"[{datetime.now()}] calculated answer: {example_answer}"
DEBUG = False
solve_problem("input.txt")
