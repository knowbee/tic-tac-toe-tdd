import unittest
from core import Game, Board
from core.game_type import HumanVsHuman

class TestGame(unittest.TestCase):
    def setUp(self):
        self.game: Game = Game()
        self.humanPlayer = HumanVsHuman()

    def test_game_has_a_board(self):
        self.assertIsInstance(self.game.board, Board)

    def test_game_has_no_player_one_at_game_start(self):
        self.assertIsNone(self.game.player_one)

    def test_game_has_no_player_two_at_game_start(self):
        self.assertIsNone(self.game.player_two)
        def test_has_current_player_symbol_property(self):
          self.assertEqual(self.game.current_player_symbol, None, "It should return None when there is no current player")

    def test_sets_current_player_symbol(self):
        self.game.current_player_symbol = "O"
        self.assertEqual(self.game.current_player_symbol, "O", "It should return O when current player is set to O")

    def test_triggered_new_turn_is_X(self):
        self.game.current_player_symbol = "O"
        self.game.handle_turns()
        self.assertEqual(self.game.current_player_symbol, "X", "It should return X when current player is handle_turnsd from O to X")

    def test_triggered_new_turn_is_O(self):
        self.game.current_player_symbol = "X"
        self.game.handle_turns()
        self.assertEqual(self.game.current_player_symbol, "O", "It should return O when current player is changed from X to O")


    def test_can_set_up_first_player_X(self):
        player_one: str = "X"
        player_two: str = "O"
        self.humanPlayer.player_one.symbol = player_one
        self.humanPlayer.player_two.symbol = player_two
        self.assertEqual(self.humanPlayer.player_one.symbol, 'X', "It should set the second player symbol to X" )
        self.assertEqual( self.humanPlayer.player_two.symbol, 'O', "It should set the second player symbol to O" )

    def test_is_win_returns_true_when_there_a_winner(self):
        self.game.board.grid = ["O", "1", "X",
                        "O", "X", "5",
                        "O", "7", "8"]
        is_a_win:bool = self.game.game_state.is_win(self.game.board)
        self.assertEqual(is_a_win, True,"It should return True when there is a winner" )

    def test_ends_game_when_symbol_O_wins(self):
        self.game.board.grid = ["O", "X", "X",
                                "O", "X", "O",
                                "O", "O", "X"]
        self.game.end_game()
        is_a_win:bool = self.game.game_state.is_win(self.game.board)
        self.assertEqual(is_a_win, True, "It should announce the player with symbol O as the player" )

    def test_returns_true_when_game_is_over_without_a_winner(self):
        self.game.board.grid = ["X", "O", "X",
                           "O", "X", "O",
                           "O", "X", "O"]
        is_a_tie:bool = self.game.game_state.tie(self.game.board)
        self.assertEqual(is_a_tie , True, "It should return True when there is a tie" )

