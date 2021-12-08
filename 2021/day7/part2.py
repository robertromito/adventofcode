# Thanks to the following for helping out:
# https://github.com/lagerfeuer/AdventOfCode2021/blob/main/day07/main.py
#
# I'm not familiar with the math for this problem and needed some help.

from datetime import datetime
import sys

DEBUG = True


def debug(*msg, **kwargs):
    if DEBUG:
        print(msg, **kwargs)


def get_input(file):
    with open(file) as f:
        return f.readline()


def fuel(c):
    return c * (c + 1) // 2


def solve_problem(input_file):
    print(f"{input_file:-^40}")

    crab_positions = [int(f) for f in get_input(input_file).split(",")]

    lowest_fuel = sys.maxsize
    for pos in range(max(crab_positions)):
        f = 0
        for crab in crab_positions:
            f += fuel(abs(crab - pos))
        if f < lowest_fuel:
            lowest_fuel = f

    answer = lowest_fuel

    print(f"[{datetime.now()}] minimum amount of fuel required to align: {answer}")
    return answer


print("=" * 40)
example_answer = solve_problem("input.example.txt")
assert example_answer == 168, f"[{datetime.now()}] calculated answer: {example_answer}"

DEBUG = False
final_answer = solve_problem("input.txt")
assert final_answer < 100347068, f"final answer of {final_answer} is too damn high"
assert final_answer > 223, f"final answer of {final_answer} is too damn low"
assert final_answer != 5066, f"final answer of {final_answer} is wrong"
