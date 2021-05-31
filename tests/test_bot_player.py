import unittest
from core import Board
from core.player import BotPlayer


class TestBot(unittest.TestCase):
    def setUp(self):
        self.bot_player = BotPlayer()
        self.board = Board()

    def test_BotPlayer_symbol_is_None(self):
        self.assertIsNone(self.bot_player.symbol)

    def test_BotPlayer_set_symbol_O_to_bot_player(self):
        self.bot_player.symbol = "O"
        self.assertEqual(self.bot_player.symbol, "O")

    def test_BotPlayer_set_symbol_X_to_bot_player(self):
        self.bot_player.symbol = "X"
        self.assertEqual(self.bot_player.symbol, "X")

    def test_Board_is_empty_when_BotPlayer_with_symbol_X_makes_a_move(self):
        self.assertTrue(self.board.is_empty())

        self.bot_player.symbol = "X"
        self.bot_player.play(self.board)

        self.assertFalse(self.board.is_empty())

    def test_BotPlayer_get_random_spot_from_available_spots(self):
        self.board.grid = ["X", "O", "X", "O", "X", "5", "O", "7", "8"]
        available_spots = self.board.get_available_spots()
        spot = self.bot_player.get_random_available_spot(self.board)
        chosen_spot_by_computer = spot in available_spots

        self.assertTrue(chosen_spot_by_computer)


if __name__ == "__main__":
    unittest.main()
