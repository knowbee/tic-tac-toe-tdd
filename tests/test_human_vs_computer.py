import unittest
from core import Board
from core.player import HumanPlayer, BotPlayer


class MockGameDiplay:
    def get_game_type(self) -> int:
        return 1

    def get_first_player(self) -> str:
        return "X"

    def get_board_size(self) -> int:
        return 3


class MockGameState:
    def tie(self, board):
        return len([s for s in board.grid if s == "X" or s == "O"]) == board.size * board.size


class MockGame:
    def __init__(self, game_display=None):
        self.game_display = MockGameDiplay
        self.board = Board(size=self.game_display.get_board_size(self))
        self.player_one = None
        self.player_two = None
        self.game_state = MockGameState

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

    def start(self):
        pass

    def play(self):
        pass

    def end_game(self):
        pass

    def handle_play(self, player):
        pass


class HumanVsComputer(MockGame):
    def __init__(self):
        super().__init__()
        self.player_one = HumanPlayer()
        self.player_two = BotPlayer()


class TestHumanVsComputer(unittest.TestCase):
    def setUp(self):
        self.game = HumanVsComputer()
        self.board = Board(size=3)

    def test_HumanVsComputer_is_Game_subclass(self):
        self.assertTrue(issubclass(HumanVsComputer, MockGame))

    def test_HumanVsComputer_inherits_play_method(self):
        self.assertIsNotNone(self.game.play)

    def test_HumanVsComputer_inherits_end_game_method(self):
        self.assertIsNotNone(self.game.end_game)

    def test_HumanVsComputer_inherits_start_method(self):
        self.assertIsNotNone(self.game.start)

    def test_HumanVsComputer_has_player_one(self):
        self.assertIsNotNone(self.game.player_one)

    def test_HumanVsComputer_has_player_two(self):
        self.assertIsNotNone(self.game.player_two)

    def test_HumanVsComputer_player_one_is_human_player_instance(self):
        self.assertIsInstance(self.game.player_one, HumanPlayer)

    def test_HumanVsComputer_player_two_is_bot_player_instance(self):
        self.assertIsInstance(self.game.player_two, BotPlayer)

    def test_Game_GameState_tie_returns_true_when_game_is_over_without_a_winner(self):
        self.game.board.grid = ["X", "O", "X", "O", "X", "O", "O", "X", "O"]
        is_a_tie: bool = self.game.game_state.tie(MockGameState, self.game.board)
        self.assertEqual(is_a_tie, True, "It should return True when there is a tie")

    def test_BotPlayer_current_player_symbol_is_X(self):
        self.assertTrue(self.board.is_empty())
        player = BotPlayer()
        player.symbol = "X"
        self.game.handle_play(player)

        # self.assertEqual(self.game.current_player_symbol, "X")


if __name__ == "__main__":
    unittest.main()
