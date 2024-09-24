from Player import Player
from board import Board

class Game:
    def __init__(self):
        self.board = Board()
        self.players = [Player("Player 1", "X"), Player("Player 2", "O")]
        self.current_player_index = 0

    def start_game(self):
        self.board.reset_board()

    def play_turn(self, row, col):
        current_player = self.players[self.current_player_index]
        if self.board.update_board(row, col, current_player.symbol):
            return current_player.name
        return None

    def check_win(self):
        board = self.board.board
        for row in board:
            if row[0] == row[1] == row[2] and row[0] != "":
                return True
        for col in range(3):
            if board[0][col] == board[1][col] == board[2][col] and board[0][col] != "":
                return True
        if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "":
            return True
        if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "":
            return True
        return False

    def check_draw(self):
        for row in self.board.board:
            if "" in row:
                return False
        return True

    def restart_game(self):
        self.board.reset_board()
        self.current_player_index = 0

    def next_turn(self):
        self.current_player_index = (self.current_player_index + 1) % 2

    def quit_game(self):
        print("Game Over")
