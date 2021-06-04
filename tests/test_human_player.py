import unittest
from core import Board
from core.player import HumanPlayer


class MockGameDiplay:
    def get_game_type(self) -> int:
        return 1

    def get_first_player(self) -> str:
        return "X"

    def get_board_size(self) -> int:
        return 3


class MockGame:
    def __init__(self, game_display=None):
        self.game_display = MockGameDiplay
        self.board = Board(size=self.game_display.get_board_size(self))
        self.player_one = None
        self.player_two = None

    def set_player_symbols(self, first_player: str) -> None:
        if first_player == "X":
            self.player_two.symbol = "O"
            self.player_one.symbol = "X"
        else:
            self.player_two.symbol = "X"
            self.player_one.symbol = "O"

    def set_game_players(self, first_player: str):
        self.set_player_symbols(first_player)
        self._initiate_current_player_symbol(first_player)

    def set_player_symbols(self, first_player: str) -> None:
        if first_player == "X":
            self.player_two.symbol = "O"
            self.player_one.symbol = "X"
        else:
            self.player_two.symbol = "X"
            self.player_one.symbol = "O"

    def _initiate_current_player_symbol(self, first_player: str) -> None:
        self.current_player_symbol = first_player


class TestHumanPlayer(unittest.TestCase):
    def setUp(self):
        self.humanPlayer = HumanPlayer()
        self.game = MockGame(game_display=MockGameDiplay)
        self.board = self.game.board

    def test_HumanPlayer_symbol_is_none_by_default(self):
        self.assertEqual(self.humanPlayer.symbol, None, "Symbol should be None when the game starts")

    def test_HumanPlayer_play_can_choose_first_grid(self):
        self.humanPlayer.play(self.board, 0)
        self.assertEqual(self.humanPlayer.symbol, self.board.grid[0], "A player should be able to pick the first spot")

    def test_HumanPlayer_play_can_choose_second_grid(self):

        self.humanPlayer.play(self.board, 1)
        self.assertEqual(self.humanPlayer.symbol, self.board.grid[1], "A player should be able to pick the second spot")

    def test_HumanPlayer_play_can_choose_third_grid(self):
        self.humanPlayer.play(self.board, 2)
        self.assertEqual(self.humanPlayer.symbol, self.board.grid[2], "A player should be able to pick the third spot")

    def test_HumanPlayer_play_can_choose_fourth_grid(self):

        self.humanPlayer.play(self.board, 3)
        self.assertEqual(self.humanPlayer.symbol, self.board.grid[3], "A player should be able to pick the fourth spot")

    def test_HumanPlayer_play_can_choose_fifth_grid(self):

        self.humanPlayer.play(self.board, 4)
        self.assertEqual(self.humanPlayer.symbol, self.board.grid[4], "A player should be able to pick the fifth spot")

    def test_HumanPlayer_play_can_choose_sixth_grid(self):

        self.humanPlayer.play(self.board, 5)
        self.assertEqual(self.humanPlayer.symbol, self.board.grid[5], "A player should be able to pick the sixth spot")

    def test_HumanPlayer_play_can_choose_seventh_grid(self):

        self.humanPlayer.play(self.board, 6)
        self.assertEqual(
            self.humanPlayer.symbol, self.board.grid[6], "A player should be able to pick the seventh spot"
        )

    def test_HumanPlayer_play_can_choose_eighth_grid(self):

        self.humanPlayer.play(self.board, 7)
        self.assertEqual(self.humanPlayer.symbol, self.board.grid[7], "A player should be able to pick the eighth spot")

    def test_HumanPlayer_play_can_choose_ninth_grid(self):

        self.humanPlayer.play(self.board, 8)
        self.assertEqual(self.humanPlayer.symbol, self.board.grid[8], "A player should be able to pick the ninth spot")

    def test_HumanPlayer_symbol_is_X(self):
        self.humanPlayer.symbol = "X"
        self.assertEqual(self.humanPlayer.symbol, "X", "Player symbol should be X when a user choose X")

    def test_HumanPlayer_symbol_is_O(self):
        self.humanPlayer.symbol = "O"
        self.assertEqual(self.humanPlayer.symbol, "O", "Player symbol should be O when a user choose O")


if __name__ == "__main__":
    unittest.main()
