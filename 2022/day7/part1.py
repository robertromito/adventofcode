from pprint import pprint

DAY = 7
PART = 1


def read_input(file) -> str:
    with open(file) as f:
        for l in f.readlines():
            yield l.strip()

def build_dir_tree(input_file: str) -> dict:
    dir_tree = {"/": {}}
    curr_dir = dir_tree["/"]
    dir_stack = []
    cmd_count = 0

    for cmd in read_input(input_file):
        cmd_count += 1
        
        print(f"[{cmd_count:3} - {cmd:20}] ", end=" ", flush=True)
        
        match cmd.split():
            case ["$", "cd", "/"]:
                dir_stack = ["/"]
                curr_dir = dir_tree["/"]

            case ["$", "cd", ".."]:
                dir_stack.pop()
                curr_dir = dir_tree
                for d in dir_stack:
                    curr_dir = curr_dir[d]

            case ["$", "cd", dir_name]:
                dir_stack.append(dir_name)
                curr_dir = curr_dir[dir_name]
            
            case ["$", "ls"]:
                pass

            case ["dir", dir_name]:
                sub_dir = curr_dir.get(dir_name, {})
                if not sub_dir:
                    curr_dir[dir_name] = sub_dir

            case _:
                file_size = int(cmd.split()[0])
                next_dir = dir_tree
                for d in dir_stack:
                    the_dir = next_dir[d]
                    the_dir['total_size'] = the_dir.get('total_size', 0) + file_size
                    next_dir = the_dir
                    
        print(dir_stack)

    return dir_tree    

def get_dir_size_points(dir_tree: dict) -> int:
    
    if isinstance(dir_tree, int):
        if dir_tree <= 100000:
            return dir_tree
        else:
            return 0

    else:
        sub_dirs_size_points = 0
        for sub_dir in dir_tree.values():
            sub_dirs_size_points += get_dir_size_points(sub_dir)

        return sub_dirs_size_points


def solve_problem(input_file: str) -> int:

    dir_tree = build_dir_tree(input_file)
    pprint(dir_tree, depth=20, indent=2, compact=False)
    
    dir_file_size_sum_total = get_dir_size_points(dir_tree["/"])

    return dir_file_size_sum_total


print(f"== day {DAY} part {PART} example", "=" * 40)
example_answer = solve_problem("input.example.txt")
assert example_answer == 95437, f"calculated answer: {example_answer}"

print(f"== day {DAY} part {PART} problem", "=" * 40)
final_answer = solve_problem("input.txt")

wrong_answers = [(0, "too low")]
for a in wrong_answers:
    assert final_answer != a[0], f"{a[0]} is wrong: {a[1]}"

print(f"final answer is: {final_answer}")
assert 1453349 == final_answer