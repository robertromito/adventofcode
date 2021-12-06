from datetime import datetime

DEBUG = True


def debug(msg, **kwargs):
    if DEBUG:
        print(msg, **kwargs)


def get_input(file):
    with open(file) as f:
        return f.readline()


def do_part2(input_file):
    print(f"{input_file:-^40}")
    lantern_fish_school = [int(f) for f in get_input(input_file).split(",")]
    debug(f"Initial state: {lantern_fish_school}")

    for i in range(80):
        for f in range(len(lantern_fish_school)):
            if lantern_fish_school[f] == 0:
                lantern_fish_school[f] = 6
                lantern_fish_school.append(8)
            else:
                lantern_fish_school[f] = lantern_fish_school[f] - 1

        debug(f"After day {i}: {len(lantern_fish_school)}")

    answer = len(lantern_fish_school)
    print(f"[{datetime.now()}] lanternfish count after 80 days: {answer}")
    return answer


print("=" * 40)
example_answer = do_part2("input.example.txt")
assert example_answer == 5934, f"[{datetime.now()}] calculated answer: {example_answer}"
DEBUG = False
do_part2("input.txt")
