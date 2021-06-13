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
        self.opponent_symbol = None

    def get_best_move(self, board):
        if board.grid[4] != "X" and board.grid[4] != "O":
            return 4
        else:
            score, move = self.alphaBetaMove(board)
            return move

    def alphaBetaMove(self, board: Board):
        cloned_board = copy.deepcopy(board)

        alpha = -1000
        beta = 1000
        score = -1000
        move = None
        opponent = None

        if self.symbol == "O":
            self.opponent_symbol = "X"
        if self.symbol == "X":
            self.opponent_symbol = "O"

        for m in cloned_board.get_available_spots():
            cloned_board.set_spot(int(m), self.opponent_symbol)

            if self.game_state.finished(cloned_board):
                return self.get_score(cloned_board), m
            else:
                current_score = self.minimizer(cloned_board, alpha, beta)
                cloned_board = copy.deepcopy(board)

                if current_score > score:
                    score = current_score
                    move = m
                alpha = max(score, alpha)

        return score, move

    def minimizer(self, board: Board, alpha, beta) -> Tuple:
        cloned_board = copy.deepcopy(board)
        best_score: int = -1000
        best_move: Optional[int] = None
        opponent = None

        for move in cloned_board.get_available_spots():
            cloned_board.set_spot(int(move), self.opponent_symbol)
            if self.game_state.finished(cloned_board):
                return self.get_score(cloned_board)
            else:
                score = self.maximizer(cloned_board, alpha, beta)
            cloned_board = copy.deepcopy(board)

            if score <= alpha:
                best_score = score
                return score

            beta = min(beta, score)
        return best_score

    def maximizer(self, board: Board, alpha, beta) -> Tuple:
        cloned_board = copy.deepcopy(board)

        best_score: int = 1000
        best_move: Optional[int] = None

        for move in cloned_board.get_available_spots():
            cloned_board.set_spot(int(move), self.symbol)
            if self.game_state.finished(cloned_board):
                return self.get_score(cloned_board)
            else:
                score = self.minimizer(cloned_board, alpha, beta)
            cloned_board = copy.deepcopy(board)

            if score >= beta:
                best_score = score
                return score
            alpha = max(alpha, score)
        return best_score

    def get_score(self, board: Board) -> int:
        winner = self.game_state.get_winner(board)
        if winner == self.symbol:
            return 1
        elif winner == self.opponent_symbol:
            return -1

        return 0

    def play(self, board: Board, **kwargs) -> int:
        move = self.get_best_move(board)
        board.set_spot(int(move), self.symbol)
        return move

    def get_random_available_spot(self, board: Board) -> int:
        available_spot = board.get_available_spots()
        return random.choice(available_spot)
