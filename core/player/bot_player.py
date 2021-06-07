import random
from .player import Player
from core import GameDisplay, Board
from typing import List
import copy
from core import GameState


class BotPlayer(Player):
    def __init__(self):
        super().__init__()
        self.game_state = GameState()
        if self.symbol == "X":
            self.opponent_symbol = "O"
        else:
            self.opponent_symbol = "X"

    def get_best_spot(self, board):
        if board.grid[4] != "X" and board.grid[4] != "O":
            return 4
        else:
            return self.maximized_spot(board)[0]

    def maximized_spot(self, board):
        clone_board = copy.deepcopy(board)

        best_score = None
        best_spot = None

        for move in clone_board.get_available_spots():
            clone_board.grid[int(move)] = self.symbol

            if self.game_state.finished(clone_board):
                score = self.get_score(clone_board)
            else:
                spot_position, score = self.minimized_spot(clone_board)

            clone_board = copy.deepcopy(board)
            if best_score == None or score > best_score:
                best_score = score
                best_spot = move
        return [best_spot, best_score]

    def minimized_spot(self, board):
        clone_board = copy.deepcopy(board)

        best_score = None
        best_spot = None
        for move in clone_board.get_available_spots():
            clone_board.grid[int(move)] = self.opponent_symbol

            if self.game_state.finished(clone_board):
                score = self.get_score(clone_board)
            else:
                spot_position, score = self.maximized_spot(clone_board)

            clone_board = copy.deepcopy(board)
            if best_score == None or score < best_score:
                best_score = score
                best_spot = move

        return [best_spot, best_score]

    def get_score(self, board):
        if self.game_state.finished(board):
            winner = self.game_state.get_winner(board)
            if winner == self.symbol:
                return 1
            elif winner == self.opponent_symbol:
                return -1
        return 0

    def play(self, board: Board, **kwargs) -> int:
        best_spot = self.get_best_spot(board)
        board.grid[int(best_spot)] = self.symbol
        return best_spot

    def get_random_available_spot(self, board: Board) -> int:
        available_spot = board.get_available_spots()
        return random.choice(available_spot)
