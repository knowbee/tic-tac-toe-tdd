from core.player import HumanPlayer, BotPlayer
from core.board import Board
from core.game_state import GameState
from core import Symbols
import os
import json


class Game:
    def __init__(self, symbol, board_size, move, ip_address):
        self.symbol = symbol
        self.move = move
        self.board = Board(board_size)
        self.game_state = GameState()
        self.bot_player = BotPlayer()
        self.unique_id = ip_address

    def play(self) -> None:
        self.set_up_symbol()
        self.create_db()

        self.human_play()
        self.bot_player.play(self.board)
        self.persist_state()

    def clean_up(self) -> None:
        if self.is_finished():
            os.remove(f"db/{self.unique_id}_current_state.json")

    @staticmethod
    def create_db() -> None:
        if not os.path.exists("db"):
            os.makedirs("db")

    def persist_state(self) -> None:
        with open(f"db/{self.unique_id}_current_state.json", "w") as current_state:
            json.dump(self.board.grid, current_state)

    def set_up_symbol(self) -> None:
        self.bot_player.symbol = Symbols[self.symbol].value

    def human_play(self) -> None:
        try:
            with open(f"db/{self.unique_id}_current_state.json") as f:
                data = json.load(f)
                self.board.grid = data
                if self.is_valid_move(self.board.grid):
                    self.board.set_spot(self.move, self.symbol)
        except Exception as e:
            self.board.set_spot(self.move, self.symbol)

    def is_valid_move(self, grid: list) -> bool:
        return grid[self.move] != Symbols[self.symbol].name and grid[self.move] != Symbols[self.symbol].value

    def is_finished(self) -> bool:
        return self.game_state.finished(self.board)

    def winner(self) -> str:
        return self.game_state.get_winner(self.board)
