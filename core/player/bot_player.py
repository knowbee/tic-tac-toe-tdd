import random
from .player import Player
from core import GameDisplay, Board, GameState
from typing import List, Optional, Tuple
import copy


class BotPlayer(Player):
    def __init__(self):
        super().__init__()
        self.game_state = GameState()
        if self.symbol == "X":
            self.opponent_symbol = "O"
        else:
            self.opponent_symbol = "X"

    def minimax(self, board: Board, player: Player, depth=0) -> Tuple:
        best_score: Optional[int] = None
        best_move: Optional[int] = None
        cloned_board = copy.deepcopy(board)
        for move in cloned_board.get_available_spots():
            cloned_board.set_spot(int(move), player)

            if self.game_state.finished(cloned_board):
                score = self.get_score(cloned_board)
                best_score = score
                best_move = move
            else:
                if player == self.symbol:
                    score, move = self.minimax(cloned_board, self.opponent_symbol, depth=depth + 1)
                    if best_score == None or score > best_score:
                        best_score = score
                        best_move = move
                else:
                    score, move = self.minimax(cloned_board, self.symbol, depth=depth + 1)
                    if best_score == None or score < best_score:
                        best_score = score
                        best_move = move
        return best_score, best_move

    def get_score(self, board):
        winner = self.game_state.get_winner(board)
        if winner == self.symbol:
            score = +1
        elif winner == self.opponent_symbol:
            score = -1
        else:
            score = 0
        return score

    def play(self, board: Board) -> int:

        score, move = self.minimax(board, self.symbol)
        board.set_spot(int(move), self.symbol)
        return move

    def get_random_available_spot(self, board: Board) -> int:
        available_spot = board.get_available_spots()
        return random.choice(available_spot)
