class Player:
    def __init__(self):
        self.symbol = None

    def set_second_symbol(self, opponent_symbol):
        if opponent_symbol == "X":
            self.symbol = "O"
        else:
            self.symbol = "X"
