from datetime import datetime


def get_input(file):
    with open(file) as f:
        return f.read().splitlines()


class VentLine:
    @staticmethod
    def scan_for_horizontal_or_vertical_lines(lines):
        hv_lines = []
        for l in lines:
            vl = VentLine(l)
            if vl.is_straight_line():
                hv_lines.append(vl)
        return hv_lines

    def __init__(self, line_def):
        c1, c2 = [c for c in line_def.split("->")]
        self.start = tuple([int(c.strip()) for c in c1.split(",")])
        self.end = tuple([int(c.strip()) for c in c2.split(",")])

    def __repr__(self):
        return f"{self.start} -> {self.end}"

    def is_straight_line(self):
        return self.start[0] == self.end[0] or self.start[1] == self.end[1]

    def get_points(self):
        if self.start[0] == self.end[0]:  # vertical
            for y in range(
                min(self.start[1], self.end[1]), max(self.start[1], self.end[1]) + 1
            ):
                yield (self.start[0], y)

        elif self.start[1] == self.end[1]:  # horizontal
            for x in range(
                min(self.start[0], self.end[0]), max(self.start[0], self.end[0]) + 1
            ):
                yield (x, self.start[1])

        else:
            raise Exception(f"line is not straight: {self}")


def do_part1(input_file):
    print(f"{input_file:-^40}")
    vent_lines = VentLine.scan_for_horizontal_or_vertical_lines(get_input(input_file))
    grid = {}
    for vl in vent_lines:
        for c in vl.get_points():
            grid[c] = grid.get(c, 0) + 1
    answer = len([p for p in grid.values() if p >= 2])
    print(
        f"[{datetime.now()}] Number of points with at least 2 overlapping lines: {answer}"
    ) 
    return answer


print("=" * 40)
example_answer = do_part1("input.example.txt")
assert example_answer == 5, f"[{datetime.now()}] calculated answer: {example_answer}"
do_part1('input.txt')

