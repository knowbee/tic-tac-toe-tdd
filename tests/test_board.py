import unittest
from core import Board


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board(size=3)

    def test_Board_grid_is_equal_to_Board_size_squared(self):
        self.board.size = 3

        self.assertEqual(
            len(self.board.grid), self.board.size ** 2, f"Game board should have {self.board.size ** 2} spots"
        )

    def test_Board_is_empty_returns_true(self):
        self.board.size = 3

        is_empty = self.board.is_empty()
        self.assertEqual(is_empty, True, "It should return true if the board is empty")

    def test_Board_is_win_returns_True_for_first_row(self):
        self.board.size = 3

        self.board.set_spot(0, "X")
        self.board.set_spot(1, "X")
        self.board.set_spot(2, "X")

        self.assertTrue(self.board.is_win(), "First row should be a win")

    def test_Board_is_win_returns_False_for_non_unique_symbols_on_first_row(self):
        self.board.size = 3

        self.board.set_spot(0, "X")
        self.board.set_spot(1, "O")
        self.board.set_spot(2, "X")

        self.assertFalse(self.board.is_win(), "Non-unique symbols should not be a win")

    def test_Board_is_win_returns_True_for_second_row(self):
        self.board.size = 3

        self.board.set_spot(3, "X")
        self.board.set_spot(4, "X")
        self.board.set_spot(5, "X")

        self.assertTrue(self.board.is_win(), "Second row should be a win")

    def test_Board_is_win_returns_True_for_third_row(self):
        self.board.size = 3

        self.board.set_spot(6, "X")
        self.board.set_spot(7, "X")
        self.board.set_spot(8, "X")

        self.assertTrue(self.board.is_win(), "Third row should be a win")

    def test_Board_is_win_returns_True_for_first_column(self):
        self.board.size = 3

        self.board.set_spot(0, "X")
        self.board.set_spot(3, "X")
        self.board.set_spot(6, "X")

        self.assertTrue(self.board.is_win(), "First column should be a win")

    def test_Board_is_win_returns_True_for_second_column(self):
        self.board.size = 3

        self.board.set_spot(1, "X")
        self.board.set_spot(4, "X")
        self.board.set_spot(7, "X")

        self.assertTrue(self.board.is_win(), "Second column should be a win")

    def test_Board_is_win_returns_True_for_third_column(self):
        self.board.size = 3

        self.board.set_spot(2, "X")
        self.board.set_spot(5, "X")
        self.board.set_spot(8, "X")

        self.assertTrue(self.board.is_win(), "Third column should be a win")
        self.board.set_spot(0, "X")
        self.board.set_spot(4, "X")
        self.board.set_spot(8, "X")

        self.assertTrue(self.board.is_win(), "Bottom left to top right diagonal should be a win")

    def test_Board_is_win_returns_True_for_top_left_to_bottom_right_diagonal(self):
        self.board.size = 3

        self.board.set_spot(2, "X")
        self.board.set_spot(4, "X")
        self.board.set_spot(6, "X")

        self.assertTrue(self.board.is_win(), "Top left to bottom right diagonal should be a win")

    def test_Board_available_spots_size_should_be_25(self):
        self.board.size = 3

        available_spots = self.board.get_available_spots()
        self.assertEqual(len(available_spots), 9, "The game board should have 9 spots in total")

    def test_Board_get_expected_winning_spot_should_return_winning_spot_in_diagonal(self):
        self.board.size = 3

        self.board.grid = ["X", "1", "2", "3", "X", "5", "6", "O", "8"]
        winning_spot = self.board.get_expected_winning_spot()
        self.assertEqual(winning_spot, 8)

    def test_Board_get_expected_winning_spot_should_return_winning_spot_in_row(self):
        self.board.size = 3

        self.board.grid = ["X", "X", "2", "3", "4", "5", "6", "O", "8"]
        winning_spot = self.board.get_expected_winning_spot()
        self.assertEqual(winning_spot, 2)

    def test_Board_get_expected_winning_spot_should_return_winning_spot_in_column(self):
        self.board.size = 3

        self.board.grid = ["X", "1", "2", "3", "4", "5", "X", "O", "8"]
        winning_spot = self.board.get_expected_winning_spot()
        self.assertEqual(winning_spot, 3)

    def test_Board_get_expected_winning_spot_should_return_None(self):
        self.board.size = 3

        self.board.grid = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
        winning_spots = self.board.get_expected_winning_spot()
        self.assertIsNone(winning_spots)

    def test_Board_reset(self):
        self.board.size = 3

        self.board.grid[4] = "X"
        self.board.reset()
        self.assertNotEqual(self.board.grid[4], "X", "The board game should have X at position 4")

    def test_Board_size_is_three(self):
        self.board.size = 3
        self.assertEqual(self.board.size, 3)

    def test_Board_size_is_five(self):
        self.board.size = 5
        self.assertEqual(self.board.size, 5)


if __name__ == "__main__":
    unittest.main()
