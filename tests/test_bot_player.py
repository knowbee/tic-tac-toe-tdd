import unittest
from core import Board
from core.player import BotPlayer


class TestBot(unittest.TestCase):
    def setUp(self):
        self.bot_player = BotPlayer()
        self.bot_player.symbol = "X"
        self.bot_player.opponent_symbol = "O"
        self.board = Board(size=3)

    def test_BotPlayer_symbol_is_Not_None(self):
        self.assertIsNotNone(self.bot_player.symbol)

    def test_BotPlayer_symbol_is_O(self):
        self.assertEqual(self.bot_player.symbol, "X")

    def test_BotPlayer_opponent_symbol_is_X(self):
        self.assertEqual(self.bot_player.opponent_symbol, "O")

    def test_BotPlayer_get_random_spot_from_available_spots(self):
        self.board.grid = ["X", "O", "X", "O", "X", "5", "O", "7", "8"]
        available_spots = self.board.get_available_spots()
        spot = self.bot_player.get_random_available_spot(self.board)
        chosen_spot_by_computer = spot in available_spots

        self.assertTrue(chosen_spot_by_computer)

    def test_BotPlayer_get_score_for_empty_board_should_be_0(self):
        self.assertEqual(self.bot_player.get_score(self.board), 0)

    def test_BotPlayer_maximizer_should_return_tuple_of_None_when_game_is_a_tie(self):
        self.board.grid = ["X", "X", "O", "O", "O", "X", "X", "X", "X"]
        self.assertEqual(self.bot_player.maximizer(self.board), (None, None))

    def test_BotPlayer_minimizer_should_return_tuple_of_None_when_game_is_a_win(self):
        self.board.grid = ["O", "X", "X", "X", "O", "O", "X", "O", "O"]
        self.assertEqual(self.bot_player.minimizer(self.board), (None, None))

    def test_BotPlayer_maximizer_should_return_1_and_8_as_best_winning_move_for_BotPlayer(self):
        self.board.grid = ["X", "O", "X",
                           "O", "X", "O",
                           "X", "O", "8"]
        self.assertEqual(self.bot_player.maximizer(self.board), (1, "8"))

    def test_BotPlayer_maximizer_should_return_minus_1_and_6_as_best_winning_move_for_BotPlayer(self):
        self.board.grid = [
            "O", "O", "X",
            "O", "X", "O",
            "6", "O", "8"]
        self.assertEqual(self.bot_player.maximizer(self.board), (-1, "6"))

    def test_BotPlayer_minimizer_should_return_minus_1_and_0_as_best_winning_move_for_HumanPlayer(self):
        self.board.grid = [
            "0", "X", "X",
            "O", "X", "5",
            "O", "7", "8"]
        self.assertEqual(self.bot_player.minimizer(self.board), (1, "0"))

    def test_BotPlayer_minimizer_should_return_1_and_3_as_best_winning_move_for_HumanPlayer(self):
        self.board.grid = [
            "O", "O", "2",
            "3", "X", "X",
            "O", "7", "O"]
        self.assertEqual(self.bot_player.minimizer(self.board), (1, "3"))


if __name__ == "__main__":
    unittest.main()
