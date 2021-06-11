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

    def test_BotPlayer_maximizer_should_return_1_and_best_spot_for_BotPlayer(self):
        self.board.grid = ["X", "O", "X", "O", "X", "5", "O", "7", "8"]
        self.assertEqual(self.bot_player.maximizer(self.board), (1, "5"))

    def test_BotPlayer_minimizer_should_return_minus_1_and_best_spot_for_HumanPlayer(self):
        self.board.grid = ["0", "O", "X", "O", "X", "5", "O", "7", "8"]
        self.assertEqual(self.bot_player.minimizer(self.board), (-1, "0"))


if __name__ == "__main__":
    unittest.main()
