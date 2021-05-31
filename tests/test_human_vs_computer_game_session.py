import unittest
from game_session import GameSession
from core import Game
from core.game_type import HumanVsHuman, HumanVsComputer
from cli import GameDisplay


class MockGameDiplay(object):
    def get_game_type(self) -> int:
        return 1

    def get_first_player(self) -> str:
        return "X"


class TestHumanVsComputerGameSession(unittest.TestCase):
    def setUp(self):

        self.game_display = MockGameDiplay()
        self.game_session: GameSession = GameSession(self.game_display)

        self.game: Game = Game()
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
