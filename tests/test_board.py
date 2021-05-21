import unittest
from core import Board

class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()

    def test_game_board_has_9_grid(self):
        self.assertEqual( len(self.board.grid), 9 , "Game board should have 9 spots")

    def test_game_board_is_empty(self):
        is_empty = self.board.is_empty()
        self.assertEqual(is_empty, True, "It should return true if the board is empty")

    def test_board_has_8_winning_combinations(self):
        self.assertEqual( len(self.board.win_combinations), 8, "The board should have 8 winning combinations")

    def test_board_has_first_winning_combination(self):
        # a_combination: list = self.board.win_combinations[0]
        self.assertEqual( self.board.win_combinations[0], [0,1,2], "First win combination should be [0,1,2]")

    def test_board_second_win_combination(self):
        self.assertEqual( self.board.win_combinations[1], [3,4,5], "Second win combination should be [3,4,5]")

    def test_board_third_win_combination(self):
        self.assertEqual( self.board.win_combinations[2], [6,7,8], "Third win combination should be [6,7,8]")

    def test_board_fourth_win_combination(self):
        self.assertEqual( self.board.win_combinations[3], [0,3,6],"Fourth win combination should be [0,3,6]")

    def test_board_fifth_win_combination(self):
        self.assertEqual( self.board.win_combinations[4], [1,4,7], "Fifth win combination should be [1,4,7]")

    def test_board_sixth_win_combination(self):
        self.assertEqual( self.board.win_combinations[5], [2,5,8], "Sixth win combination should be [2,5,8]")

    def test_board_seventh_win_combination(self):
        self.assertEqual( self.board.win_combinations[6], [0,4,8], "Seventh win combination should be [0,4,8]")

    def test_board_eigth_win_combination(self):
        self.assertEqual( self.board.win_combinations[7], [2,4,6] , "Eight win combination should be [2,4,6]")

    def test_board_available_spots(self):
        available_spots = self.board.get_available_spots()
        self.assertEqual( len(available_spots), 9, "The game board should have 9 spots in total" )

    def test_board_can_be_reset(self):
        self.board.grid[4] = 'X'
        self.board.reset()
        self.assertNotEqual( self.board.grid[4], 'X', "The board game should have X at position 4")

if __name__ == '__main__':
    unittest.main()
