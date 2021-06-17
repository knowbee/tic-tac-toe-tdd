import random
from .player import Player
from core import GameDisplay, Board
from core.minimax import MiniMax
from typing import List, Optional, Tuple
import copy
import math


class BotPlayer(Player):
    def __init__(self):
        super().__init__()

    def play(self, board: Board, **kwargs) -> int:
        minimax = MiniMax(self.symbol)
        score, move = minimax.get_best_score(board)
        board.set_spot(int(move), self.symbol)
        return move

    def get_random_available_spot(self, board: Board) -> int:
        available_spot = board.get_available_spots()
        return random.choice(available_spot)
