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

    def set_up(self):
        if self.symbol == "X":
            self.opponent_symbol = "O"
        else:
            self.opponent_symbol = "X"

    def alpha_beta_prunning(self, board, alpha, beta):
        cloned_board = copy.deepcopy(board)
        return self.maximizer_alpha_beta_prunning(cloned_board, alpha, beta)

    def minimax(self, board: Board, is_max) -> Tuple:

        cloned_board = copy.deepcopy(board)
        if is_max:
            return self.maximizer(cloned_board)
        return self.minimizer(cloned_board)

    def minimizer_alpha_beta_prunning(self, board: Board, alpha, beta) -> Tuple:
        best_score: int = 100
        best_move: Optional[int] = None
        cloned_board = copy.deepcopy(board)

        for move in cloned_board.get_available_spots():
            cloned_board.set_spot(int(move), self.symbol)
            if self.game_state.finished(cloned_board):
                return self.get_score(cloned_board), move
            else:
                score, move_position = self.alpha_beta_prunning(cloned_board, alpha, beta)
                if score < best_score:
                    best_move = move
                    best_score = score

                if score <= alpha:
                    return score, move
                if score < beta:
                    beta = score
                cloned_board = copy.deepcopy(board)

        return best_score, best_move

    def maximizer_alpha_beta_prunning(self, board: Board, alpha, beta):

        best_score: int = -100
        best_move: Optional[int] = None
        cloned_board = copy.deepcopy(board)

        for move in cloned_board.get_available_spots():
            cloned_board.set_spot(int(move), self.opponent_symbol)
            if self.game_state.finished(cloned_board):
                return self.get_score(cloned_board), int(move)
            else:
                score, move_position = self.alpha_beta_prunning(cloned_board, alpha, beta)
                if score > best_score:
                    best_move = move
                    best_score = score

                if score >= beta:
                    return best_score, move

                if score > alpha:
                    alpha = score
                cloned_board = copy.deepcopy(board)
        return best_score, best_move

    def minimizer(self, board):
        best_score: Optional[int] = None
        best_move: Optional[int] = None
        cloned_board = copy.deepcopy(board)

        for move in cloned_board.get_available_spots():
            cloned_board.set_spot(int(move), self.symbol)
            if self.game_state.finished(cloned_board):
                score = self.get_score(cloned_board)
            else:
                score, move_position = self.minimax(cloned_board, True)
            cloned_board = copy.deepcopy(board)

            if best_score == None or score > best_score:
                best_score = score
                best_move = move

        return best_score, best_move

    def maximizer(self, board):
        best_score: Optional[int] = None
        best_move: Optional[int] = None
        cloned_board = copy.deepcopy(board)

        for move in cloned_board.get_available_spots():
            cloned_board.set_spot(int(move), self.opponent_symbol)
            if self.game_state.finished(cloned_board):
                score = self.get_score(cloned_board)
            else:
                score, move_position = self.minimax(cloned_board, False)
            cloned_board = copy.deepcopy(board)

            if best_score == None or score < best_score:
                best_score = score
                best_move = move

        return best_score, best_move

    def get_score(self, board: Board) -> int:
        if self.game_state.finished(board):
            winner = self.game_state.get_winner(board)
            if winner == self.symbol:
                return 1
            elif winner == self.opponent_symbol:
                return -1

        return 0

    def play(self, board: Board, **kwargs) -> int:
        self.set_up()
        # score, move = self.minimax(board, False)
        score, move = self.alpha_beta_prunning(board, -100, 100)
        board.set_spot(int(move), self.symbol)
        return move

    def get_random_available_spot(self, board: Board) -> int:
        available_spot = board.get_available_spots()
        return random.choice(available_spot)
