from datetime import datetime

print("=" * 40)


def get_input(file):
    with open(file) as f:
        return f.read().splitlines()


class Board:
    def __init__(self, number, board_rows):
        self.number = number
        self.board = []
        self.unmarked_score = 0
        self.winner = False
        self.winning_score = None
        self.winning_number = None
        self.matches = []
        for r in board_rows:
            row = [int(n) for n in r.split()]
            self.unmarked_score += sum(row)
            self.board.append(row)

    def __str__(self):
        val = (
            f"board {self.number} | "
            f"winner: {self.winner} | "
            f"score: {self.winning_score} | "
            f"winning number: {self.winning_number}\n"
            f"matches: {self.matches}\n"
        )
        for r in self.board:
            for c in r:
                val += f"{c:>7} "
            val += "\n"

        return val

    def won(self, drawn_number):
        self.winner = True
        self.winning_score = self.unmarked_score * drawn_number
        self.winning_number = drawn_number
        return self.winning_score

    def draw(self, drawn_number: int):
        if self.winner:
            return
        col_marked_count = [0] * 5
        for r in range(5):
            row_marked_count = 0
            for c in range(5):
                if self.board[r][c] == drawn_number:
                    self.matches.append(drawn_number)
                    self.board[r][c] = f"{drawn_number}({len(self.matches)})"
                    self.unmarked_score -= drawn_number

                if type(self.board[r][c]) == str:
                    row_marked_count += 1
                    col_marked_count[c] += 1

            if row_marked_count == 5:
                return self.won(drawn_number)

        if [c for c in col_marked_count if c == 5]:
            return self.won(drawn_number)

        return False


def do_part1(input_file):
    print(f"{input_file:-^40}")
    numbers_to_draw, *raw_boards = get_input(input_file)
    boards = []
    board_rows = []
    board_number = 1
    for l in raw_boards[1:]:
        if l:
            board_rows.append(l)
        else:
            boards.append(Board(board_number, board_rows))
            board_rows = []
            board_number += 1
    boards.append(Board(board_number, board_rows))

    for n in numbers_to_draw.split(","):
        for b in boards:
            if result := b.draw(int(n)):
                print(b)
                return result

    raise Exception("no winners!")


example_answer = do_part1("input.example.txt")
assert example_answer == 4512, f"calculated answer: {example_answer}"

print(f"[{datetime.now()}] Final score of winning board: {do_part1('input.txt')}")
