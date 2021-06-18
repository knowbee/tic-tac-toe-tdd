import unittest
import copy
from core import Board, GameState
from core.player.bot_player.minimax import MiniMax
from typing import List, Optional, Tuple
from enum import Enum


class TestMiniMax(unittest.TestCase):
    def setUp(self):
        self.minimax = MiniMax("X")
        self.board = Board(3)

    def test_MiniMax_get_score_for_empty_board_should_be_0(self):
        self.assertEqual(self.minimax.get_score(self.board), 0)

    def test_MiniMax_maximizer_should_return_tuple_of_None_when_game_is_a_tie(self):
        self.board.grid = ["X", "X", "O", "O", "O", "X", "X", "X", "X"]
        self.assertEqual(self.minimax.maximizer(self.board, -100, 100), (-100, None))

    def test_MiniMax_minimizer_should_return_tuple_of_None_when_game_is_a_win(self):
        self.board.grid = ["O", "X", "X", "X", "O", "O", "X", "O", "O"]
        self.assertEqual(self.minimax.minimizer(self.board, -100, 100), (100, None))

    def test_MiniMax_maximizer_should_return_1_and_8_as_best_winning_move_for_BotPlayer(self):
        self.board.grid = ["X", "O", "X", "O", "X", "O", "X", "O", "8"]
        self.assertEqual(self.minimax.maximizer(self.board, -100, 100), (1, 8))

    def test_MiniMax_maximizer_should_return_1_and_6_as_best_winning_move_for_BotPlayer(self):
        self.board.grid = ["O", "O", "X", "O", "X", "O", "6", "O", "8"]
        self.assertEqual(self.minimax.maximizer(self.board, -100, 100), (1, 6))

    def test_MiniMax_minimizer_should_return_minus_1_and_0_as_best_winning_move_for_HumanPlayer(self):
        self.board.grid = ["0", "X", "X", "O", "X", "5", "O", "7", "8"]
        self.assertEqual(self.minimax.minimizer(self.board, -100, 100), (-1, 0))

    def test_MiniMax_minimizer_should_return_minus_1_and_2_as_best_winning_move_for_HumanPlayer(self):
        self.board.grid = ["O", "O", "2", "3", "X", "X", "O", "7", "O"]
        self.assertEqual(self.minimax.minimizer(self.board, -100, 100), (-1, 2))

    def test_MiniMax_minmax_choose_fourth_spot(self):
        self.assertEqual(self.minimax.get_best_spot(self.board), (None, 4))


if __name__ == "__main__":
    unittest.main()
