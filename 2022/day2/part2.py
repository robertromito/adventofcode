def read_input(file):
    with open(file) as f:
        return f.readlines()


def solve_problem(input_file):
    
    COUNTER = {
        "X": "LOSE",
        "Y": "DRAW",
        "Z": "WIN"
    }

    POINTS = {
        "A LOSE": 0 + 3, 
        "A DRAW": 3 + 1, 
        "A WIN": 6 + 2,
        "B LOSE": 0 + 1, 
        "B DRAW": 3 + 2, 
        "B WIN": 6 + 3,
        "C LOSE": 0 + 2, 
        "C DRAW": 3 + 3, 
        "C WIN": 6 + 1,
    }

    score = 0

    for r in read_input(input_file):
        move, outcome = r.split()

        score += POINTS[f"{move} {COUNTER[outcome]}"]

    return score


print("== day 2 part 1 ", "=" * 40)
example_answer = solve_problem("input.example.txt")
assert example_answer == 12, f"calculated answer: {example_answer}"

final_answer = solve_problem("input.txt")
print(f"final answer is: {final_answer}")
