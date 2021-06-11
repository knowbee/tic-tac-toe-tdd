import random
from .player import Player
from core import GameDisplay, Board, GameState
from typing import List, Optional, Tuple
import copy
import math


class BotPlayer(Player):
    def __init__(self):
        super().__init__()
        self.game_state = GameState()
        if self.symbol == "X":
            self.opponent_symbol = "O"
        else:
            self.opponent_symbol = "X"

    def minimizer(self, board: Board) -> Tuple:
        cloned_board = copy.deepcopy(board)

        best_score: Optional[int] = None
        best_move: Optional[int] = None

        for move in cloned_board.get_available_spots():
            cloned_board.set_spot(int(move), self.opponent_symbol)
            if self.game_state.finished(cloned_board):
                score = self.get_score(cloned_board)
            else:
                score, move_position = self.maximizer(cloned_board)
            cloned_board = copy.deepcopy(board)

            if best_score == None or score < best_score:
                best_score = score
                best_move = move
                return best_score, best_move
        return best_score, best_move

    def maximizer(self, board: Board) -> Tuple:
        cloned_board = copy.deepcopy(board)

        best_score: Optional[int] = None
        best_move: Optional[int] = None

        for move in cloned_board.get_available_spots():
            cloned_board.set_spot(int(move), self.symbol)
            if self.game_state.finished(cloned_board):
                score = self.get_score(cloned_board)
            else:
                score, move_position = self.minimizer(cloned_board)
            cloned_board = copy.deepcopy(board)

            if best_score == None or score > best_score:
                best_score = score
                best_move = move
                return best_score, best_move

        return best_score, best_move

    def get_score(self, board: Board) -> int:
        winner = self.game_state.get_winner(board)
        if winner == self.symbol:
            return 1
        elif winner == self.opponent_symbol:
            return -1

        return 0

    def play(self, board: Board, **kwargs) -> int:

        score, move = self.maximizer(board)
        print("opponent", self.opponent_symbol)
        board.set_spot(int(move), self.symbol)
        return move

    def get_random_available_spot(self, board: Board) -> int:
        available_spot = board.get_available_spots()
        return random.choice(available_spot)
