from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QLabel, QMessageBox
import sys

class View(QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Tic-Tac-Toe')
        
        # Set background color to black
        self.setStyleSheet("background-color: #20c997;")

        self.grid_layout = QGridLayout()
        self.buttons = [[QPushButton() for _ in range(3)] for _ in range(3)]

        for i in range(3):
            for j in range(3):
                self.buttons[i][j].setFixedSize(140, 140)
                self.buttons[i][j].setStyleSheet("font-size: 30px; color: #20c997;")
                self.buttons[i][j].clicked.connect(lambda _, row=i, col=j: self.on_click(row, col))
                self.grid_layout.addWidget(self.buttons[i][j], i, j)

        self.status_label = QLabel('Player 1\'s turn')
        self.status_label.setStyleSheet("color: white;")  # Status label text color to white
        self.grid_layout.addWidget(self.status_label, 3, 0, 1, 3)

        self.setLayout(self.grid_layout)

    def on_click(self, row, col):
        current_player = self.controller.play_turn(row, col)
        if current_player:
            symbol = self.controller.players[self.controller.current_player_index].symbol
            
            # Set color based on symbol ("X" -> blue, "O" -> red)
            if symbol == "X":
                self.buttons[row][col].setStyleSheet("color: blue; font-size: 40px;")
            else:
                self.buttons[row][col].setStyleSheet("color: red; font-size: 40px;")
                
            self.buttons[row][col].setText(symbol)
            
            if self.controller.check_win():
                self.show_winner(current_player)
            elif self.controller.check_draw():
                self.show_draw()
            else:
                self.controller.next_turn()
                self.update_display()

    def update_display(self):
        next_player = self.controller.players[self.controller.current_player_index].name
        self.status_label.setText(f"{next_player}'s turn")

    def show_winner(self, winner):
        QMessageBox.information(self, 'Game Over', f'{winner} wins!')
        self.controller.restart_game()
        self.reset_board()

    def show_draw(self):
        QMessageBox.information(self, 'Game Over', 'It\'s a draw!')
        self.controller.restart_game()
        self.reset_board()

    def reset_board(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].setText('')
                self.buttons[i][j].setStyleSheet("color: white; font-size: 40px;")  # Reset to default color


# Rest of the code remains the same (controller logic, etc.)
