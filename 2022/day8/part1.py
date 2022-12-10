from dataclasses import dataclass

DAY = 8
PART = 1


@dataclass(frozen=True)
class TreeVisibleFrom:
    position: tuple
    height: int
    top: bool
    left: bool
    right: bool
    bottom: bool

    def is_visible(self):
        return self.top or self.left or self.right or self.bottom

    def __repr__(self):
        top_vis = "T" if self.top else ""
        left_vis = "L" if self.left else ""
        right_vis = "R" if self.right else ""
        bottom_vis = "B" if self.bottom else ""

        return f"[{self.position} {self.height} {top_vis:1}{left_vis:1}{right_vis:1}{bottom_vis:1}]"


def read_input(file) -> str:
    with open(file) as f:
        for l in f.readlines():
            yield [int(t) for t in l.strip()]


def solve_problem(input_file: str) -> int:

    forest = [row for row in read_input(input_file)]
    row_length = len(forest[0])
    col_length = len(forest)

    number_of_visible_trees = 0
    for row in range(row_length):
        for col in range(col_length):
            same_row = forest[row]
            same_col = [r[col] for r in forest]
            tree_height = forest[row][col]
            
            tv = TreeVisibleFrom(
                top=(row == 0) or (tree_height > max(same_col[:row])),
                left=(col == 0) or (tree_height > max(same_row[:col])),
                right=(col == col_length - 1) or (tree_height > max(same_row[col+1:])),
                bottom=(row == row_length - 1) or (tree_height > max(same_col[row+1:])),
                position=(row, col),
                height=tree_height,
            )

            # print(tv, end=" ", flush=True)
            
            if (row == 0):
                assert tv.top, f"top row tree should be visible: {tv}"
            if (row == (row_length - 1)):
                assert tv.bottom, f"bottom row tree should be visible: {tv}"
            if (col == 0):
                assert tv.left, f"left col tree should be visible: {tv}"
            if (col == (col - 1)):
                assert tv.right, f"right col tree should be visible: {tv}"


            if tv.is_visible():
                number_of_visible_trees += 1

        # print()

    return number_of_visible_trees


print(f"== day {DAY} part {PART} example", "=" * 40)
example_answer = solve_problem("input.example.txt")
assert example_answer == 21, f"calculated answer: {example_answer}"
print(f"example answer is: {example_answer}")


print(f"== day {DAY} part {PART} problem", "=" * 40)
final_answer = solve_problem("input.txt")

wrong_answers = []
for a in wrong_answers:
    assert final_answer != a[0], f"{a[0]} is wrong: {a[1]}"

print(f"final answer is: {final_answer}")
assert 1711 == final_answer
