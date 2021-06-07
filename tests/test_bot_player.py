import unittest
from core import Board
from core.player import BotPlayer


class TestBot(unittest.TestCase):
    def setUp(self):
        self.bot_player = BotPlayer()
        self.board = Board(size=3)

    def test_BotPlayer_symbol_is_None(self):
        self.assertIsNone(self.bot_player.symbol)

    def test_BotPlayer_set_symbol_O_to_bot_player(self):
        self.bot_player.symbol = "O"
        self.assertEqual(self.bot_player.symbol, "O")

    def test_BotPlayer_set_symbol_X_to_bot_player(self):
        self.bot_player.symbol = "X"
        self.assertEqual(self.bot_player.symbol, "X")

    def test_bot_player_minimized_spot_returns_best_spot_and_best_score(self):
        self.bot_player.symbol = "X"
        self.board.grid = [
            "0", "O", "X", 
            "O", "X", "5", 
            "O", "7", "8"]
        self.assertEqual(self.bot_player.minimized_spot(self.board), ["0", 1])


if __name__ == "__main__":
    unittest.main()
