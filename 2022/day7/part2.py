from pprint import pprint

DAY = 7
PART = 1

TOTAL_DISK_SPACE = 70000000
NEEDED_FREE_SPACE = 30000000

def read_input(file) -> str:
    with open(file) as f:
        for l in f.readlines():
            yield l.strip()

def build_dir_tree(input_file: str) -> tuple:
    total_used_space = 0
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
                total_used_space += file_size
                next_dir = dir_tree
                for d in dir_stack:
                    the_dir = next_dir[d]
                    the_dir['total_size'] = the_dir.get('total_size', 0) + file_size
                    next_dir = the_dir
                    
        print(dir_stack)

    return (total_used_space, dir_tree)

def get_smallest_dir_to_free_up(space_needed: int, dir_tree: dict) -> int:
    
    if isinstance(dir_tree, int):
        if dir_tree >= space_needed:
            return dir_tree
        else:
            return 0

    else:
        sub_dirs_size_points = [TOTAL_DISK_SPACE]
        for sub_dir in dir_tree.values():
            space_freed = get_smallest_dir_to_free_up(space_needed, sub_dir)
            if space_freed >= space_needed:
                sub_dirs_size_points.append(space_freed)

        return min(sub_dirs_size_points)


def solve_problem(input_file: str) -> int:

    used_space, dir_tree = build_dir_tree(input_file)
    pprint(dir_tree, depth=20, indent=2, compact=False)

    space_to_delete = NEEDED_FREE_SPACE - (TOTAL_DISK_SPACE - used_space)
    print(f"space to delete: {space_to_delete}")
    
    return get_smallest_dir_to_free_up(space_to_delete, dir_tree["/"])



print(f"== day {DAY} part {PART} example", "=" * 40)
example_answer = solve_problem("input.example.txt")
assert example_answer == 24933642, f"calculated answer: {example_answer}"

print(f"== day {DAY} part {PART} problem", "=" * 40)
final_answer = solve_problem("input.txt")

wrong_answers = [(0, "too low")]
for a in wrong_answers:
    assert final_answer != a[0], f"{a[0]} is wrong: {a[1]}"

print(f"final answer is: {final_answer}")
assert 2948823 == final_answer