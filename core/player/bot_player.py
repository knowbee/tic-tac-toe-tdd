import random
from .player import Player
from core import GameDisplay, Board
from typing import List


class BotPlayer(Player):
    def __init__(self):
        super().__init__()

    def play(self, board):
        winning_spot = board.almost_a_winning_spot()
        if winning_spot is not None and len(winning_spot) != 0:
            board.grid[winning_spot[0]] = self.symbol
            return winning_spot[0]
        random_spot = int(self.get_random_available_spot(board))
        board.grid[random_spot] = self.symbol
        return random_spot

    def get_random_available_spot(self, board: Board) -> int:
        available_spot = board.get_available_spots()
        return random.choice(available_spot)
