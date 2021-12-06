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
    initial_lantern_fish_school = [int(f) for f in get_input(input_file).split(",")]
    lantern_fish_school = [0] * 9

    for f in initial_lantern_fish_school:
        lantern_fish_school[f] = lantern_fish_school[f] + 1

    debug(f"Initial state: {lantern_fish_school}")

    for day in range(256):
        new_lantern_fish = lantern_fish_school[0]
        lantern_fish_school[0] = lantern_fish_school[1]
        lantern_fish_school[1] = lantern_fish_school[2]
        lantern_fish_school[2] = lantern_fish_school[3]
        lantern_fish_school[3] = lantern_fish_school[4]
        lantern_fish_school[4] = lantern_fish_school[5]
        lantern_fish_school[5] = lantern_fish_school[6]
        lantern_fish_school[6] = lantern_fish_school[7] + new_lantern_fish
        lantern_fish_school[7] = lantern_fish_school[8]
        lantern_fish_school[8] = new_lantern_fish

        debug(f"day {day}: total: {sum(lantern_fish_school)} created: {new_lantern_fish}")

    answer = sum(lantern_fish_school)
    print(f"[{datetime.now()}] lanternfish count after 80 days: {answer}")
    return answer


print("=" * 40)
example_answer = do_part2("input.example.txt")
assert (
    example_answer == 26984457539
), f"[{datetime.now()}] calculated answer: {example_answer}"
DEBUG = False
do_part2("input.txt")
