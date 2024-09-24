from PyQt5.QtWidgets import QApplication
import sys
from game import Game
from view import View

if __name__ == "__main__":
    app = QApplication(sys.argv)
    game = Game()
    view = View(game)
    view.show()
    sys.exit(app.exec_())
