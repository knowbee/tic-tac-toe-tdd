import unittest
from core import Board
from core.player import BotPlayer


class TestBot(unittest.TestCase):
  def setUp(self):
    self.bot_player = BotPlayer()
    self.board = Board()

  def test_bot_player_has_no_symbol(self):
    self.assertIsNone(self.bot_player.symbol)

  def test_bot_player_set_symbol_O(self):
    self.bot_player.symbol = "O"
    self.assertEqual(self.bot_player.symbol,  "O")

  def test_bot_player_set_symbol_X(self):
    self.bot_player.symbol = "X"
    self.assertEqual(self.bot_player.symbol,  "X")

  def test_board_not_empty_when_bot_player_as_symbol_X_makes_a_move(self):
      self.assertTrue(self.board.is_empty())

      self.bot_player.symbol = "X"
      self.bot_player.play(self.board)

      self.assertFalse(self.board.is_empty())

if __name__ == "__main__":
  unittest.main()