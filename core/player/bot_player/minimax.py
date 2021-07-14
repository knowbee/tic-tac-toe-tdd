import copy
from core.board import Board
from core.game_state import GameState
from typing import List, Optional, Tuple
from ..symbols import Symbols
from enum import Enum


class MiniMax:
    def __init__(self, symbol):
        self.game_state = GameState()
        self.symbol = Symbols(symbol)
        self.max_move = None
        self.min_move = None
        self.alpha = -100
        self.beta = 100

        self.min_score = 100
        self.max_score = -100

    def get_best_spot(self, board: Board) -> Tuple:
        cloned_board = copy.deepcopy(board)
        if board.grid[4] != self.symbol.name and board.grid[4] != self.symbol.value:
            return None, 4
        return self.maximizer(cloned_board, self.alpha, self.beta)

    def minimizer(self, board: Board, alpha: int, beta: int) -> Tuple:
        cloned_board = copy.deepcopy(board)
        for move in cloned_board.get_available_spots():
            cloned_board.set_spot(int(move), self.symbol.name)
            if self.terminal_state(cloned_board):
                return self.get_score(cloned_board), int(move)
            score = self.maximizer(cloned_board, alpha, beta)[0]
            self.update_min_state(score, move)

            if self.can_prune_min(score, alpha):
                return score, move

            if self.can_update_beta(score, beta):
                beta = score

            cloned_board = copy.deepcopy(board)
        return self.min_score, self.min_move

    def maximizer(self, board: Board, alpha: int, beta: int) -> Tuple:
        cloned_board = copy.deepcopy(board)
        for move in cloned_board.get_available_spots():
            cloned_board.set_spot(int(move), self.symbol.value)
            if self.terminal_state(cloned_board):
                return self.get_score(cloned_board), int(move)
            score = self.minimizer(cloned_board, alpha, beta)[0]
            self.update_max_state(score, move)

            if self.can_prune_max(score, beta):
                return beta, move

            if self.can_update_alpha(score, beta):
                alpha = score

            cloned_board = copy.deepcopy(board)
        return self.max_score, self.max_move

    def can_prune_max(self, score: int, beta: int) -> bool:
        return score >= beta

    def can_prune_min(self, score: int, alpha: int) -> bool:
        return score <= alpha

    def can_update_alpha(self, score: int, alpha: int) -> bool:
        return score > alpha

    def can_update_beta(self, score: int, beta: int) -> bool:
        return score < beta

    def update_max_state(self, score: int, move: int) -> None:
        if score > self.max_score:
            self.max_move = move
            self.max_score = score

    def update_min_state(self, score: int, move: int) -> None:
        if score < self.min_score:
            self.min_move = move

    def terminal_state(self, board: Board) -> bool:
        return self.game_state.finished(board)

    def get_score(self, board: Board) -> int:
        if self.game_state.finished(board):
            winner = self.game_state.get_winner(board)
            if winner == self.symbol.value:
                return 1
            elif winner == self.symbol.name:
                return -1
        return 0
