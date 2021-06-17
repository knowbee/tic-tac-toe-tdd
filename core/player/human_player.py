from .player import Player
from core.symbols import Symbols


class HumanPlayer(Player):
    def __init__(self):
        super().__init__()

    def play(self, board, spot):
        if board.grid[spot] != Symbols.X.name and board.grid[spot] != Symbols.O.name:
            board.grid[spot] = self.symbol
        else:
            board.grid[spot] = None
