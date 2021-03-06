import unittest
from game_session import GameSession
from core import Game, Board
from core.game_type import HumanVsComputer
from cli import GameDisplay
from core.player import HumanPlayer


class MockGameDisplay:
    def get_game_type(self) -> int:
        return 0

    def get_first_player(self) -> str:
        return "X"

    def get_board_size(self) -> int:
        return 3


class MockGame:
    def __init__(self, game_display=None):
        self.game_display = MockGameDisplay
        self.board = Board(size=self.game_display.get_board_size(self))
        self.player_one = None
        self.player_two = None

    def set_player_symbols(self, first_player: str) -> None:
        if first_player == "X":
            self.player_two.symbol = "O"
            self.player_one.symbol = "X"
        else:
            self.player_two.symbol = "X"
            self.player_one.symbol = "O"

    def set_game_players(self, first_player: str):
        self.set_player_symbols(first_player)
        self._initiate_current_player_symbol(first_player)

    def set_player_symbols(self, first_player: str) -> None:
        if first_player == "X":
            self.player_two.symbol = "O"
            self.player_one.symbol = "X"
        else:
            self.player_two.symbol = "X"
            self.player_one.symbol = "O"

    def _initiate_current_player_symbol(self, first_player: str) -> None:
        self.current_player_symbol = first_player


class HumanVsHuman(MockGame):
    def __init__(self):
        super().__init__()
        self.player_one = HumanPlayer()
        self.player_two = HumanPlayer()


class TestHumanVsHumanGameSession(unittest.TestCase):
    def setUp(self):
        self.game_display = MockGameDisplay()
        self.game_session: GameSession = GameSession(self.game_display)
        self.human_vs_human = HumanVsHuman()

    def test_when_HumanVsHuman_set_player_symbols_to_O_player_one_symbol_should_be_O(self):
        self.human_vs_human.set_player_symbols("O")
        self.assertEqual(
            self.human_vs_human.player_one.symbol, "O", "If the first player is O, player one symbol should be O"
        )
        self.assertEqual(
            self.human_vs_human.player_two.symbol, "X", "If the first player is X, player one symbol should be X"
        )

    def test_when_HumanVsHuman_set_player_symbols_to_X_player_one_symbol_should_be_X(self):
        self.human_vs_human.set_player_symbols("X")
        self.assertEqual(
            self.human_vs_human.player_one.symbol, "X", "If the first player is X, player one symbol should be X"
        )
        self.assertEqual(
            self.human_vs_human.player_two.symbol, "O", "If the first player is O, player one symbol should be O"
        )

    def test_HumanVsHuman_set_game_players_to_X_player_one_symbol_should_be_X(self):
        self.human_vs_human.set_game_players("X")

        self.assertEqual("X", self.human_vs_human.player_one.symbol, "Incorrect symbol for first player.")
        self.assertEqual("O", self.human_vs_human.player_two.symbol, "Incorrect symbol for second player.")

    def test_HumanVsHuman_set_game_players_to_X_current_player_symbol_should_be_X(self):
        self.human_vs_human.set_game_players("X")
        self.assertEqual("X", self.human_vs_human.current_player_symbol, "Incorrect current player symbol.")
