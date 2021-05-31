import unittest
from core import Board


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_game_board_has_9_grid(self):
        self.assertEqual(len(self.board.grid), 9, "Game board should have 9 spots")

    def test_game_board_is_empty(self):
        is_empty = self.board.is_empty()
        self.assertEqual(is_empty, True, "It should return true if the board is empty")

    def test_board_has_8_winning_combinations(self):
        self.assertEqual(len(self.board.win_combinations), 8, "The board should have 8 winning combinations")

    def test_Board_is_win_returns_True_for_first_row(self):
        self.board.set_spot(0, "X")
        self.board.set_spot(1, "X")
        self.board.set_spot(2, "X")

        self.assertTrue(self.board.is_win(), "First row should be a win")

    def test_Board_is_win_returns_False_for_non_unique_symbols_on_first_row(self):
        self.board.set_spot(0, "X")
        self.board.set_spot(1, "O")
        self.board.set_spot(2, "X")

        self.assertFalse(self.board.is_win(), "Non-unique symbols should not be a win")

    def test_Board_is_win_returns_True_for_second_row(self):
        self.board.set_spot(3, "X")
        self.board.set_spot(4, "X")
        self.board.set_spot(5, "X")

        self.assertTrue(self.board.is_win(), "Second row should be a win")

    def test_Board_is_win_returns_True_for_third_row(self):
        self.board.set_spot(6, "X")
        self.board.set_spot(7, "X")
        self.board.set_spot(8, "X")

        self.assertTrue(self.board.is_win(), "Third row should be a win")

    def test_Board_is_win_returns_True_for_first_column(self):
        self.board.set_spot(0, "X")
        self.board.set_spot(3, "X")
        self.board.set_spot(6, "X")

        self.assertTrue(self.board.is_win(), "First column should be a win")

    def test_Board_is_win_returns_True_for_second_column(self):
        self.board.set_spot(1, "X")
        self.board.set_spot(4, "X")
        self.board.set_spot(7, "X")

        self.assertTrue(self.board.is_win(), "Second column should be a win")

    def test_Board_is_win_returns_True_for_third_column(self):
        self.board.set_spot(2, "X")
        self.board.set_spot(5, "X")
        self.board.set_spot(8, "X")

        self.assertTrue(self.board.is_win(), "Third column should be a win")

    def test_Board_is_win_returns_True_for_first_diagonal(self):
        self.board.set_spot(0, "X")
        self.board.set_spot(4, "X")
        self.board.set_spot(8, "X")

        self.assertTrue(self.board.is_win(), "First diagonal should be a win")

    def test_Board_is_win_returns_True_for_second_diagonal(self):
        self.board.set_spot(2, "X")
        self.board.set_spot(4, "X")
        self.board.set_spot(6, "X")

        self.assertTrue(self.board.is_win(), "Second diagonal should be a win")

    def test_board_available_spots(self):
        available_spots = self.board.get_available_spots()
        self.assertEqual(len(available_spots), 9, "The game board should have 9 spots in total")

    def test_board_can_be_reset(self):
        self.board.grid[4] = "X"
        self.board.reset()
        self.assertNotEqual(self.board.grid[4], "X", "The board game should have X at position 4")


if __name__ == "__main__":
    unittest.main()
