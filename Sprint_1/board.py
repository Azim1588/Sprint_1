class Board:
    def __init__(self, size=3):
        self.size = size
        self.board = [["" for _ in range(size)] for _ in range(size)]

    def display_board(self):
        for row in self.board:
            print(row)

    def update_board(self, row, col, symbol):
        if self.board[row][col] == "":
            self.board[row][col] = symbol
            return True
        return False

    def reset_board(self):
        self.board = [["" for _ in range(self.size)] for _ in range(self.size)]
