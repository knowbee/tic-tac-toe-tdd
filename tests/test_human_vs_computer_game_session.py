import unittest
from game_session import GameSession
from core import Game, Board
from cli import GameDisplay
from core.player import HumanPlayer, BotPlayer


class MockGameDisplay:
    def get_game_type(self) -> int:
        return 1

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


class HumanVsComputer(MockGame):
    def __init__(self):
        super().__init__()
        self.player_one = HumanPlayer()
        self.player_two = BotPlayer()


class TestHumanVsComputerGameSession(unittest.TestCase):
    def setUp(self):

        self.game_display = MockGameDisplay()
        self.game_session: GameSession = GameSession(self.game_display)
        self.game: MockGame = MockGame()
        self.human_vs_computer = HumanVsComputer()

    def test_when_HumanVsComputer_set_player_symbol_to_O_then_player_one_symbol_should_be_O(self):
        self.human_vs_computer.set_player_symbols("O")
        self.assertEqual(
            self.human_vs_computer.player_one.symbol, "O", "If the first player is O, player one symbol should be O"
        )
        self.assertEqual(
            self.human_vs_computer.player_two.symbol, "X", "If the first player is X, player one symbol should be X"
        )

    def test_when_HumanVsComputer_set_player_symbol_to_X_then_player_one_symbol_should_be_X(self):
        self.human_vs_computer.set_player_symbols("X")
        self.assertEqual(
            self.human_vs_computer.player_one.symbol, "X", "If the first player is X, player one symbol should be X"
        )
        self.assertEqual(
            self.human_vs_computer.player_two.symbol, "O", "If the first player is O, player one symbol should be O"
        )

    def test_if_HumanVsComputer_set_player_symbols_first_player_X_current_player_symbol_should_be_X_when_game_starts(
        self,
    ):
        first_player = "X"
        self.game.current_player_symbol = first_player
        self.human_vs_computer.set_player_symbols(first_player)
        self.assertEqual(
            self.game.current_player_symbol, "X", "If first player is X, current player symbol should be X"
        )

    def test_HumanVsComputer_set_game_players_X_player_one_symbol_should_be_X(self):
        self.human_vs_computer.set_game_players("X")

        self.assertEqual("X", self.human_vs_computer.player_one.symbol, "Incorrect symbol for first player.")
        self.assertEqual("O", self.human_vs_computer.player_two.symbol, "Incorrect symbol for second player.")

    def test_HumanVsComputer_set_game_players_X_current_player_symbol_X(self):
        self.human_vs_computer.set_game_players("X")

        self.assertEqual("X", self.human_vs_computer.current_player_symbol, "Incorrect current player symbol.")
