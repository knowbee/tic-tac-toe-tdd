import unittest
from core import GameState, Board


class TestGameState(unittest.TestCase):
    def setUp(self):
        self.gameState = GameState()
        self.board = Board()
        self.board.size = 3

    def test_GameState_finished_returns_false_when_the_game_is_still_going_on(self):
        self.board.set_board_grid()
        is_finished: bool = self.gameState.finished(self.board)
        self.assertEqual(is_finished, False, "It should return false for an empty board")

    def test_GameState_finished_returns_True_the_board_is_full_with_a_winner(self):
        self.board.set_board_grid()
        self.board.grid = ["O", "1", "X", "O", "X", "5", "O", "7", "8"]
        is_finished: bool = self.gameState.finished(self.board)
        self.assertEqual(is_finished, True, "It should return True if the game is finished with the winner")

    def test_GameState_finished_returns_True_when_the_board_is_full_with_a_tie(self):
        self.board.set_board_grid()

        self.board.grid = ["X", "O", "X", "O", "X", "O", "O", "X", "O"]
        is_finished: bool = self.gameState.finished(self.board)
        self.assertEqual(is_finished, True, "It should return True if the game is finished with a Tie")

    def test_GameState_get_winner_returns_O_as_a_winner(self):
        self.board.set_board_grid()

        self.board.grid = ["O", "1", "X", "O", "X", "5", "O", "7", "8"]
        winner: str = self.gameState.get_winner(self.board)
        self.assertEqual(winner, "O", "It should return O as the winner")

    def test_GameState_get_winner_returns_X_as_a_winner(self):
        self.board.set_board_grid()

        self.board.grid = ["X", "1", "O", "X", "O", "5", "X", "7", "8"]
        winner: str = self.gameState.get_winner(self.board)
        self.assertEqual(winner, "X", "It should return X as the winner")


if __name__ == "__main__":
    unittest.main()
