import unittest
import core
from core.player import HumanPlayer

class TestHumanPlayer(unittest.TestCase):

    def setUp(self):
        self.humanPlayer = HumanPlayer()
        self.board = core.Board()

    def test_humanPlayer_symbol_is_none_by_default(self):
        self.assertEqual( self.humanPlayer.symbol, None, "Symbol should be None when the game starts" )

    def test_humanPlayer_can_choose_first_grid(self):
        self.humanPlayer.play(self.board, 0)
        self.assertEqual( self.humanPlayer.symbol, self.board.grid[0], "A player should be able to pick the first spot")

    def test_humanPlayer_can_choose_second_grid(self):
        self.humanPlayer.play(self.board, 1)
        self.assertEqual( self.humanPlayer.symbol, self.board.grid[1], "A player should be able to pick the second spot")

    def test_humanPlayer_can_choose_third_grid(self):
        self.humanPlayer.play(self.board, 2)
        self.assertEqual( self.humanPlayer.symbol, self.board.grid[2], "A player should be able to pick the third spot")

    def test_humanPlayer_can_choose_fourth_grid(self):
        self.humanPlayer.play(self.board, 3)
        self.assertEqual( self.humanPlayer.symbol, self.board.grid[3], "A player should be able to pick the fourth spot")

    def test_humanPlayer_can_choose_fifth_grid(self):
        self.humanPlayer.play(self.board, 4)
        self.assertEqual( self.humanPlayer.symbol, self.board.grid[4], "A player should be able to pick the fifth spot")

    def test_humanPlayer_can_choose_sixth_grid(self):
        self.humanPlayer.play(self.board, 5)
        self.assertEqual( self.humanPlayer.symbol, self.board.grid[5], "A player should be able to pick the sixth spot")

    def test_humanPlayer_can_choose_seventh_grid(self):
        self.humanPlayer.play(self.board, 6)
        self.assertEqual( self.humanPlayer.symbol, self.board.grid[6], "A player should be able to pick the seventh spot")

    def test_humanPlayer_can_choose_eighth_grid(self):
        self.humanPlayer.play(self.board, 7)
        self.assertEqual( self.humanPlayer.symbol, self.board.grid[7], "A player should be able to pick the eighth spot")

    def test_humanPlayer_can_choose_ninth_grid(self):
        self.humanPlayer.play(self.board, 8)
        self.assertEqual( self.humanPlayer.symbol, self.board.grid[8], "A player should be able to pick the ninth spot")

    def test_humanPlayer_symbol_is_X(self):
        self.humanPlayer.symbol = 'X'
        self.assertEqual( self.humanPlayer.symbol, 'X', "Player symbol should be X when a user choose X")

    def test_humanPlayer_symbol_is_O(self):
        self.humanPlayer.symbol = 'O'
        self.assertEqual( self.humanPlayer.symbol, 'O',  "Player symbol should be O when a user choose O")
if __name__ == '__main__':
    unittest.main()
