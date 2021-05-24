import unittest
from game_session import GameSession
import core
from core.game_type import HumanVsHuman
from cli import GameDisplay


class MockGameDiplay(object):
    def get_game_type(self) -> int:
        return 0

    def get_first_player(self) -> str:
        return 'X'


class TestGameSession(unittest.TestCase):
    def setUp(self):
        self.game_display = MockGameDiplay()
        self.game_session: GameSession = GameSession(
            HumanVsHuman(), self.game_display)
        self.game: core.Game = core.Game()
        self.humanPlayer = HumanVsHuman()

    def test_when_first_player_is_O_player_one_symbol_should_be_O(self):
        self.game_session.set_player_symbols("O")
        self.assertEqual(self.game_session.human_vs_human.playerOne.symbol,
                         "O", "If the first player is O, player one symbol should be O")
        self.assertEqual(self.game_session.human_vs_human.playerTwo.symbol,
                         "X", "If the first player is X, player one symbol should be X")

    def test_when_first_player_is_X_player_one_symbol_should_be_X(self):
        self.game_session.set_player_symbols("X")
        self.assertEqual(self.game_session.human_vs_human.playerOne.symbol,
                         "X", "If the first player is X, player one symbol should be X")
        self.assertEqual(self.game_session.human_vs_human.playerTwo.symbol,
                         "O", "If the first player is O, player one symbol should be O")

    def test_if_first_player_X_current_player_symbol_should_be_X_when_game_starts(self):
        first_player = "X"
        self.game.current_player_symbol = first_player
        self.game_session.set_player_symbols(first_player)
        self.assertEqual(self.game.current_player_symbol, "X",
                         "If first player is X, current player symbol should be X")

    def test_set_game_session_sets_players_symbols(self):
        self.game_session.set_game_players('X')

        self.assertEqual('X', self.game_session.human_vs_human.playerOne.symbol,
                         'Incorrect symbol for first player.')
        self.assertEqual('O', self.game_session.human_vs_human.playerTwo.symbol,
                         'Incorrect symbol for second player.')

    def test_game_should_have_first_player_as_current_player_symbol(self):
        self.game_session.set_game_players('X')

        self.assertEqual('X', self.game_session.human_vs_human.current_player_symbol,
                         'Incorrect current player symbol.')

    def test_get_match_should_return_game_with_players_set(self):
        game: HumanVsHuman = self.game_session.get_match()

        self.assertEqual('X', game.playerOne.symbol, 'Incorrect first player')
        self.assertEqual('O', game.playerTwo.symbol,
                         'Incorrect second player')
