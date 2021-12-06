from datetime import datetime

DEBUG = False

def dprint(msg, **kwargs):
    if DEBUG: print(msg, **kwargs)

def get_input(file):
    with open(file) as f:
        return f.read().splitlines()


class VentLine:
    def __init__(self, line_def):
        c1, c2 = [c for c in line_def.split("->")]
        self.start = tuple([int(c.strip()) for c in c1.split(",")])
        self.end = tuple([int(c.strip()) for c in c2.split(",")])

    def __repr__(self):
        return f"{self.start} -> {self.end}"

    def is_horizontal(self):
        return self.start[1] == self.end[1]

    def is_vertical(self):
        return self.start[0] == self.end[0]

    def is_diagonal(self):
        return abs(self.start[0] - self.end[0]) == abs(self.start[1] - self.end[1])

    def get_points(self):

        if self.is_vertical():
            dprint(f"{self} is vertical")
            for y in range(
                min(self.start[1], self.end[1]), max(self.start[1], self.end[1]) + 1
            ):
                yield (self.start[0], y)

        elif self.is_horizontal():
            dprint(f"{self} is horizontal")
            for x in range(
                min(self.start[0], self.end[0]), max(self.start[0], self.end[0]) + 1
            ):
                yield (x, self.start[1])

        elif self.is_diagonal():
            dprint(f"{self} is diagonal - ", end="")
            # top left -> bottom right : 0,0 -> 3,3
            if (self.start[0] < self.end[0]) and (self.start[1] < self.end[1]):
                line_segments = self.end[0] - self.start[0]
                dprint(f"tlbr [{line_segments}]")
                yield tuple(self.start)
                for p in range(1, line_segments):
                    yield (self.start[0] + p, self.start[1] + p)
                yield tuple(self.end)

            # bottom left -> top right : 0,9 -> 3,6
            elif (self.start[0] < self.end[0]) and (self.start[1] > self.end[1]):
                line_segments = self.end[0] - self.start[0]
                dprint(f"bltr [{line_segments}]")
                yield tuple(self.start)
                for p in range(1, line_segments):
                    yield (self.start[0] + p, self.start[1] - p)
                yield tuple(self.end)

            # top right -> bottom left : 9,0 -> 6,3
            elif (self.start[0] > self.end[0]) and (self.start[1] < self.end[1]):
                line_segments = self.start[0] - self.end[0]
                dprint(f"trbl [{line_segments}]")
                yield tuple(self.start)
                for p in range(1, line_segments):
                    yield (self.start[0] - p, self.start[1] + p)
                yield tuple(self.end)

            # bottom right -> top left : 9,9 -> 6,6
            elif (self.start[0] > self.end[0]) and (self.start[1] > self.end[1]):
                line_segments = self.start[0] - self.end[0]
                dprint(f"brtl [{line_segments}]")
                yield tuple(self.start)
                for p in range(1, line_segments):
                    yield (self.start[0] - p, self.start[1] - p)
                yield tuple(self.end)

            else:
                dprint("unknown")
            
        
        else:
            dprint(f"{self} is unknown")


def visualize(points):
    #my_print(points)
    max_x = max([c[0] for c in points.keys()]) + 1
    max_y = max([c[1] for c in points.keys()]) + 1
    for y in range(max_y):
        for x in range(max_x):
            dprint(points.get((x,y), '.'), end="")
        dprint("")
    dprint("")


def do_part2(input_file):
    print(f"{input_file:-^40}")
    vent_lines = [VentLine(vl) for vl in get_input(input_file)]
    grid = {}
    for vl in vent_lines:
        for c in vl.get_points():
            dprint(c)
            grid[c] = grid.get(c, 0) + 1
    answer = len([p for p in grid.values() if p >= 2])
    visualize(grid)
    print(
        f"[{datetime.now()}] Number of points with at least 2 overlapping lines: {answer}"
    )
    return answer


print("=" * 40)
example_answer = do_part2("input.example.txt")
assert example_answer == 12, f"[{datetime.now()}] calculated answer: {example_answer}"
do_part2("input.txt")
