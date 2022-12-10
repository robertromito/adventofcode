from dataclasses import dataclass
from pprint import pprint

DAY = 8
PART = 2


def read_input(file) -> str:
    with open(file) as f:
        for l in f.readlines():
            yield [int(t) for t in l.strip()]


@dataclass(frozen=True)
class TreeScenicScore:
    position: tuple
    height: int
    top: int
    left: int
    right: int
    bottom: int

    def a_score(self, direction):
        score = 0
        
        for tree_height in direction:
            score += 1
            if tree_height >= self.height:
                break

        return score

    def score(self):

        assert len(self.top) == self.position[0]
        assert len(self.left) == self.position[1]

        return (
            self.a_score(self.top)
            * self.a_score(self.left)
            * self.a_score(self.right)
            * self.a_score(self.bottom)
        )


    def __repr__(self):
        return f"{self.position} {self.height} {self.score():3}"


def solve_problem(input_file: str) -> int:

    forest = [row for row in read_input(input_file)]
    # pprint(forest)

    row_length = len(forest[0])
    col_length = len(forest)

    max_scenic_score = 0

    for row in range(row_length):

        # print("| ", end="", flush=True)

        for col in range(col_length):
            same_row = forest[row]
            same_col = [r[col] for r in forest]

            tv = TreeScenicScore(
                top=list(reversed(same_col[:row])),
                left=list(reversed(same_row[:col])),
                right=same_row[col + 1 :],
                bottom=same_col[row + 1 :],
                position=(row, col),
                height=forest[row][col],
            )


            if tv.score() > max_scenic_score:
                max_scenic_score = tv.score()

            # print(tv, f"[{max_scenic_score}]", end=" | ", flush=True)

        # print()

    return max_scenic_score


print(f"== day {DAY} part {PART} example", "=" * 40)
example_answer = solve_problem("input.example.txt")
assert example_answer == 8, f"calculated answer: {example_answer}"
print(f"example answer is: {example_answer}")


print(f"== day {DAY} part {PART} problem", "=" * 40)
final_answer = solve_problem("input.txt")

wrong_answers = []
for a in wrong_answers:
    assert final_answer != a[0], f"{a[0]} is wrong: {a[1]}"

print(f"final answer is: {final_answer}")
assert 301392 == final_answer
