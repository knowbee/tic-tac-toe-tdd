import copy
from core import Board, GameState
from typing import List, Optional, Tuple
from core.symbols import Symbols
from enum import Enum


class MiniMax:
    def __init__(self, symbol):
        self.game_state = GameState()
        self.symbol = Symbols(symbol)
        self.max_move = None
        self.min_move = None
        self.beta = -100
        self.alpha = 100

    def get_best_score(self, board):
        cloned_board = copy.deepcopy(board)
        if board.grid[4] != self.symbol.name and board.grid[4] != self.symbol.value:
            return None, 4
        return self.maximizer(cloned_board, self.alpha, self.beta)

    def minimizer(self, board: Board, alpha, beta) -> Tuple:
        cloned_board = copy.deepcopy(board)
        for move in cloned_board.get_available_spots():
            cloned_board.set_spot(int(move), self.symbol.name)
            if self.terminal_state(cloned_board):
                return self.get_score(cloned_board), int(move)
            score = int(self.get_current_max_score(cloned_board, alpha, beta))
            if score < beta:
                beta = score
            self.update_min_state(score, move)
            self.prune_min(alpha, move)
            cloned_board = copy.deepcopy(board)
        return self.alpha, self.min_move

    def maximizer(self, board: Board, alpha, beta):
        cloned_board = copy.deepcopy(board)
        for move in cloned_board.get_available_spots():
            cloned_board.set_spot(int(move), self.symbol.value)
            if self.terminal_state(cloned_board):
                return self.get_score(cloned_board), int(move)
            score = int(self.get_current_min_score(cloned_board, alpha, beta))
            if score > alpha:
                alpha = score

            self.update_max_state(score, move)
            self.prune_max(beta, move)
            cloned_board = copy.deepcopy(board)
        return self.beta, self.max_move

    def get_current_min_score(self, board, alpha, beta):
        return self.minimizer(board, alpha, beta)[0]

    def get_current_max_score(self, board, alpha, beta):
        return self.maximizer(board, alpha, beta)[0]

    def update_min_state(self, score, move):
        if score < self.alpha:
            self.min_move = move

    def update_max_state(self, score, move):
        if score > self.beta:
            self.max_move = move
            self.beta = score

    def terminal_state(self, board):
        return self.game_state.finished(board)

    def prune_max(self, beta, move):
        if self.beta >= beta:
            return self.beta, move

    def prune_min(self, alpha, move):
        if self.alpha <= alpha:
            return self.alpha, move

    def get_score(self, board: Board) -> int:
        if self.game_state.finished(board):
            winner = self.game_state.get_winner(board)
            if winner == self.symbol.value:
                return 1
            elif winner == self.symbol.name:
                return -1

        return 0
