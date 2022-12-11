# Thanks for the help https://www.reddit.com/user/ElliotDG/!
# https://www.reddit.com/r/adventofcode/comments/zgnice/comment/izq9wcn/?context=3

from dataclasses import dataclass, field

DAY = 9
PART = 2


def read_input(file) -> str:
    with open(file) as f:
        for l in f.readlines():
            yield l.strip().split()


@dataclass
class Head:
    x: int = 0
    y: int = 0

    def step(self, dir):
        x_move = 1 if dir in ["L", "R"] else 0
        x_dir = -1 if dir == "L" else 1

        y_move = 1 if dir in ["U", "D"] else 0
        y_dir = -1 if dir == "D" else 1

        self.x += x_move * x_dir
        self.y += y_move * y_dir
        self.last_dir = dir

    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"


@dataclass
class Tail:
    x: int = 0
    y: int = 0
    visits: set = field(default_factory=set, hash=False)

    def follow(self, knot):
        dist_x, dist_y = knot.x - self.x, knot.y - self.y

        if (abs(dist_x) < 2) and (abs(dist_y) < 2):
            # don't need to move
            return
        elif abs(dist_x) == 2 and not dist_y:
            # horizontal
            xv = 1 if dist_x > 0 else -1
            self.x += xv
        elif abs(dist_y) == 2 and not dist_x:
            # vertical
            yv = 1 if dist_y > 0 else -1
            self.y += yv
        elif (abs(dist_y) == 2 and abs(dist_x) in (1, 2)) or (
            abs(dist_x) == 2 and abs(dist_y) in (1, 2)
        ):
            # diagonal
            xv = 1 if dist_x > 0 else -1
            self.x += xv
            yv = 1 if dist_y > 0 else -1
            self.y += yv

        self.visits.add((self.x, self.y))

    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"


def solve_problem(input_file: str) -> int:

    head = Head()
    TAIL = 8
    tails = []
    for _ in range(TAIL + 1):
        t = Tail()
        t.visits.add((0, 0))
        tails.append(t)

    assert len(tails) == 9, "tails weren't created properly"

    for dir, moves in read_input(input_file):
        # print(f"{head} -> {dir} {moves} -> ", end="", flush=True)
        for _ in range(int(moves)):
            head.step(dir)
            knot_to_follow = head
            for t in tails:
                t.follow(knot_to_follow)
                knot_to_follow = t
        # for t in tails:
        #     print(f"{t}", end=" ", flush=True)
        # print()

    return len(tails[TAIL].visits)


print(f"== day {DAY} part {PART} example", "=" * 40)
example_answer = solve_problem("input.example.part2.txt")
assert example_answer == 36, f"calculated answer: {example_answer}"
print(f"example answer is: {example_answer}")

print(f"== day {DAY} part {PART} problem", "=" * 40)
final_answer = solve_problem("input.txt")

wrong_answers = []
for a in wrong_answers:
    assert final_answer != a[0], f"{a[0]} is wrong: {a[1]}"

print(f"final answer is: {final_answer}")
assert 2545 == final_answer
