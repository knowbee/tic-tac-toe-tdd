import unittest
import core
from core.game_type import HumanVsHuman

class TestGame(unittest.TestCase):
    def setUp(self):
        self.game: core.Game = core.Game()
        self.humanPlayer = HumanVsHuman()

    def test_game_has_a_board(self):
        self.assertIsInstance(self.game.board, core.Board)

    def test_game_has_handle_turns(self):
        self.assertIsInstance(self.game.handleTurns, core.HandleTurns)

    def test_game_has_no_player_one_at_game_start(self):
        self.assertIsNone(self.game.playerOne)

    def test_game_has_no_player_two_at_game_start(self):
        self.assertIsNone(self.game.playerTwo)

    def test_can_set_up_first_player_X(self):
        player_one: str = "X"
        player_two: str = "O"
        self.humanPlayer.playerOne.symbol = player_one
        self.humanPlayer.playerTwo.symbol = player_two
        self.assertEqual(self.humanPlayer.playerOne.symbol, 'X', "It should set the second player symbol to X" )
        self.assertEqual( self.humanPlayer.playerTwo.symbol, 'O', "It should set the second player symbol to O" )

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

