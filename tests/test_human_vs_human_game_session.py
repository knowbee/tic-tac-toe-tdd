import unittest
from game_session import GameSession
from core import Game
from core.game_type import HumanVsHuman, HumanVsComputer
from cli import GameDisplay


class MockGameDiplay(object):
    def get_game_type(self) -> int:
        return 0

    def get_first_player(self) -> str:
        return "X"


class TestHumanVsHumanGameSession(unittest.TestCase):
    def setUp(self):
        self.game_display = MockGameDiplay()
        self.game_session: GameSession = GameSession(self.game_display)
        self.game: Game = Game()
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

    def test_GameSession_get_match_should_return_game_with_players_set(self):
        game: HumanVsHuman = self.game_session.get_match()

        self.assertEqual("X", game.player_one.symbol, "Incorrect first player")
        self.assertEqual("O", game.player_two.symbol, "Incorrect second player")
