import unittest
from core import Game, Board
from core.game_type import HumanVsHuman


class TestGame(unittest.TestCase):
    def setUp(self):
        self.game: Game = Game()
        self.humanPlayer = HumanVsHuman()

    def test_Game_has_a_board(self):
        self.assertIsInstance(self.game.board, Board)

    def test_Game_has_no_player_one_when_Game_is_initiated(self):
        self.assertIsNone(self.game.player_one)

    def test_Game_has_no_player_two_when_game_is_initiated(self):
        self.assertIsNone(self.game.player_two)

        def test_Game_current_player_symbol__is_None_when_Game_is_initiated(self):
            self.assertEqual(
                self.game.current_player_symbol, None, "It should return None when there is no current player"
            )

    def test_Game_current_player_symbol_is_set_to_O(self):
        self.game.current_player_symbol = "O"
        self.assertEqual(self.game.current_player_symbol, "O", "It should return O when current player is set to O")

    def test_Game_handle_turns_sets_current_player_to_O(self):
        self.game.current_player_symbol = "O"
        self.game.handle_turns()
        self.assertEqual(
            self.game.current_player_symbol, "X", "It should return X when current player is handle_turnsd from O to X"
        )

    def test_handle_turns_sets_current_player_to_X(self):
        self.game.current_player_symbol = "X"
        self.game.handle_turns()
        self.assertEqual(
            self.game.current_player_symbol, "O", "It should return O when current player is changed from X to O"
        )

    def test_Game_GameState_tie_returns_true_when_game_is_over_without_a_winner(self):
        self.game.board.grid = ["X", "O", "X", "O", "X", "O", "O", "X", "O"]
        is_a_tie: bool = self.game.game_state.tie(self.game.board)
        self.assertEqual(is_a_tie, True, "It should return True when there is a tie")
