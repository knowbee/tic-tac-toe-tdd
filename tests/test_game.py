import unittest
from core import Board
from core.player import HumanPlayer


class MockGameDisplay:
    def get_game_type(self) -> int:
        return 0

    def get_first_player(self) -> str:
        return "X"

    def get_board_size(self) -> int:
        return 3


class MockGameState:
    def tie(self, board):
        return len([s for s in board.grid if s == "X" or s == "O"]) == board.size * board.size


class MockGame:
    def __init__(self, game_display=None):
        self.game_display = MockGameDisplay
        self.board = Board(size=self.game_display.get_board_size(self))
        self.player_one = None
        self.player_two = None
        self.current_player_symbol = None
        self.game_state = MockGameState

    def handle_turns(self):
        if self.current_player_symbol == "X":
            self.current_player_symbol = "O"
        else:
            self.current_player_symbol = "X"

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


class HumanVsHuman(MockGame):
    def __init__(self):
        super().__init__()
        self.player_one = HumanPlayer()
        self.player_two = HumanPlayer()


class TestGame(unittest.TestCase):
    def setUp(self):
        self.game_display = MockGameDisplay()
        self.game: Game = MockGame()
        self.humanPlayer = HumanVsHuman()

    def test_Game_has_a_board(self):
        self.assertIsInstance(self.game.board, Board)

    def test_Game_has_no_player_one_when_Game_is_initiated(self):
        self.assertIsNone(self.game.player_one)

    def test_Game_has_no_player_two_when_game_is_initiated(self):
        self.assertIsNone(self.game.player_two)

        def test_Game_current_player_symbol__is_None_when_Game_is_initiated(self):
            self.assertEqual(
                self.game.current_player_symbol, None, "It should return None when there is no current player"
            )

    def test_Game_current_player_symbol_is_set_to_O(self):
        self.game.current_player_symbol = "O"
        self.assertEqual(self.game.current_player_symbol, "O", "It should return O when current player is set to O")

    def test_Game_handle_turns_sets_current_player_to_O(self):
        self.game.current_player_symbol = "O"
        self.game.handle_turns()
        self.assertEqual(
            self.game.current_player_symbol, "X", "It should return X when current player is handle_turnsd from O to X"
        )

    def test_handle_turns_sets_current_player_to_X(self):
        self.game.current_player_symbol = "X"
        self.game.handle_turns()
        self.assertEqual(
            self.game.current_player_symbol, "O", "It should return O when current player is changed from X to O"
        )

    def test_Game_GameState_tie_returns_true_when_game_is_over_without_a_winner(self):
        self.game.board.grid = ["X", "O", "X", "O", "X", "O", "O", "X", "O"]
        is_a_tie: bool = self.game.game_state.tie(MockGameState, self.game.board)
        self.assertEqual(is_a_tie, True, "It should return True when there is a tie")
