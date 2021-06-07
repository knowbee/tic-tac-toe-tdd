from .player import Player


class HumanPlayer(Player):
    def __init__(self):
        super().__init__()

    def play(self, board, spot=None):
        if board.grid[spot] != "X" and board.grid[spot] != "O":
            board.grid[spot] = self.symbol
        else:
            board.grid[spot] = None
