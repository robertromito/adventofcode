def read_input(file):
    with open(file) as f:
        return f.readlines()


def solve_problem(input_file):
    elves = [0]
    current_elf = 0
    for l in read_input(input_file):
        l = l.strip()
        if l:
            elves[current_elf] += int(l)
        else:
            current_elf += 1
            elves.append(0)

    return max(elves)


print("== part 1 ", "=" * 40)
example_answer = solve_problem("input.example.txt")
print(f"example answer is: {example_answer}")
assert example_answer == 24000, f"calculated answer: {example_answer}"

final_answer = solve_problem("input.txt")
print(f"final answer is: {final_answer}")
