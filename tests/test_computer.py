import unittest
from core import Board
from core.player import BotPlayer

class TestComputer(unittest.TestCase):
  def setUp(self):
    self.board: Board = Board()
    self.computer: BotPlayer = BotPlayer()

  def test_computer_has_symbol(self):
    self.assertIsNone(self.computer.symbol)

  def test_computer_can_get_random_spot_from_available_spots(self):
    self.board.grid = ["X", "O", "X", "O", "X", "5", "O", "7", "8"]
    available_spots = self.board.get_available_spots()
    spot = self.computer.get_random_available_spot(self.board)
    chosen_spot_by_computer = spot in available_spots

    self.assertTrue(chosen_spot_by_computer)

if __name__ == "__main__":
  unittest.main()