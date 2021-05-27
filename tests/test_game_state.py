import unittest
from core import GameState,  Board

class TestGameState(unittest.TestCase):

    def setUp(self):
        self.gameState = GameState();
        self.board = Board();

    def test_game_is_not_finished(self):
        is_finished: bool = self.gameState.finished(self.board)
        self.assertEqual(is_finished, False,"It should return false for an empty board")

    def test_game_is_finished_with_a_winner(self):
        self.board.grid = ["O", "1", "X",
                           "O", "X", "5",
                           "O", "7", "8"]
        is_finished: bool = self.gameState.finished(self.board)
        self.assertEqual(is_finished, True ,"It should return True if the game is finished with the winner")

    def test_game_is_finished_with_a_tie(self):
        self.board.grid = ["X", "O", "X",
                           "O", "X", "O",
                           "O", "X", "O"]
        is_finished: bool = self.gameState.finished(self.board)
        self.assertEqual( is_finished, True, "It should return True if the game is finished with a Tie" )

    def test_get_winner_returns_O_as_a_winner(self):
        self.board.grid = ["O", "1", "X",
                           "O", "X", "5",
                           "O", "7", "8"]
        winner: str = self.gameState.get_winner(self.board)
        self.assertEqual(winner, "O", "It should return O as the winner" )

    def test_get_winner_returns_X_as_a_winner(self):
        self.board.grid = ["X", "1", "O",
                           "X", "O", "5",
                           "X", "7", "8"]
        winner: str = self.gameState.get_winner(self.board)
        self.assertEqual(winner, "X", "It should return X as the winner" )

    def test_check_is_a_win_returns_false_on_empty_board(self):
        is_a_win: bool = self.gameState.is_win(self.board)
        self.assertEqual(is_a_win, False, "It should return False on empty board" )

    def test_returns_true_when_there_is_a_winner(self):
        self.board.grid = ["O", "1", "X",
                           "O", "X", "5",
                           "O", "7", "8"]
        is_a_win: bool = self.gameState.is_win(self.board)
        self.assertEqual(is_a_win , True,"It should return True when there is a winner" )

    def test_is_winning_combination_returns_false_with_combination_one_on_empty_board(self):
        is_a_winning_combination: bool = self.gameState.is_winning_combination(self.board.win_combinations[0], self.board.grid)
        self.assertEqual(is_a_winning_combination, False, "It should return False on empty board for the first combination")

    def test_is_winning_combination_returns_false_with_combination_two_on_empty_board(self):
        is_a_winning_combination: bool = self.gameState.is_winning_combination(self.board.win_combinations[1], self.board.grid)
        self.assertEqual( is_a_winning_combination, False, "It should return False on empty board for the second combination")

    def test_is_winning_combination_returns_false_with_combination_three_on_empty_board(self):
        is_a_winning_combination: bool = self.gameState.is_winning_combination(self.board.win_combinations[2], self.board.grid)
        self.assertEqual(is_a_winning_combination , False, "It should return False on empty board for the third combination")

    def test_is_winning_combination_returns_false_with_combination_four_on_empty_board(self):
        is_a_winning_combination: bool = self.gameState.is_winning_combination(self.board.win_combinations[3], self.board.grid)

        self.assertEqual( is_a_winning_combination, False, "It should return False on empty board for the fourth combination")

    def test_is_winning_combination_returns_false_with_combination_five_on_empty_board(self):
        is_a_winning_combination: bool = self.gameState.is_winning_combination(self.board.win_combinations[4], self.board.grid)

        self.assertEqual( is_a_winning_combination, False, "It should return False on empty board for the fifth combination")

    def test_is_winning_combination_returns_false_with_combination_six_on_empty_board(self):
        is_a_winning_combination: bool = self.gameState.is_winning_combination(self.board.win_combinations[5], self.board.grid)

        self.assertEqual( is_a_winning_combination, False, "It should return False on empty board for the sixth combination")

    def test_is_winning_combination_returns_false_with_combination_seven_on_empty_board(self):
        is_a_winning_combination: bool = self.gameState.is_winning_combination(self.board.win_combinations[6], self.board.grid)

        self.assertEqual( is_a_winning_combination, False, "It should return False on empty board for the seventh combination")

    def test_is_winning_combination_returns_false_with_combination_eight_on_empty_board(self):
        is_a_winning_combination: bool = self.gameState.is_winning_combination(self.board.win_combinations[7], self.board.grid)

        self.assertEqual( is_a_winning_combination, False, "It should return False on empty board for the eight combination")

if __name__ == '__main__':
    unittest.main()
