class Player:
    def __init__(self, name="", symbol=""):
        self.name = name
        self.symbol = symbol

    def choose_name(self, name):
        self.name = name

    def choose_symbol(self, symbol):
        self.symbol = symbol
