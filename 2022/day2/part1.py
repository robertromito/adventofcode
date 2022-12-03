def read_input(file):
    with open(file) as f:
        return f.readlines()


def solve_problem(input_file):
    
    POINTS = {
        "A X": 3 + 1, 
        "A Y": 6 + 2, 
        "A Z": 0 + 3,
        "B X": 0 + 1, 
        "B Y": 3 + 2, 
        "B Z": 6 + 3,
        "C X": 6 + 1, 
        "C Y": 0 + 2, 
        "C Z": 3 + 3,
    }

    score = 0

    for r in read_input(input_file):
        score += POINTS[r.strip()]

    return score


print("== day 2 part 1 ", "=" * 40)
example_answer = solve_problem("input.example.txt")
assert example_answer == 15, f"calculated answer: {example_answer}"

final_answer = solve_problem("input.txt")
print(f"final answer is: {final_answer}")
