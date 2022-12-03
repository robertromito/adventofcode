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
    return sum(sorted(elves,reverse=True)[0:3])


print("== part 2 ", "=" * 40)
example_answer = solve_problem("input.example.txt")
print(f"example answer is: {example_answer}")
assert example_answer == 45000, f"calculated answer: {example_answer}"

print(f"final answer is: {solve_problem('input.txt')}")
