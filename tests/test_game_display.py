import unittest
from cli import GameDisplay
from core import Board
from core.player import HumanPlayer, BotPlayer


class MockGameDisplay:
    def __init__(self):
        self.message = None

    def get_board_size(self):
        self.message = "What board size you want to play?"
        return 3


class MockGame:
    def __init__(self, player_one, player_two, game_display=None):
        self.game_display = MockGameDisplay
        self.board = Board(size=self.game_display.get_board_size(self))
        self.player_one = player_one
        self.player_two = player_two


class TestGameDisplay(unittest.TestCase):
    def setUp(self):
        self.game = MockGame(player_one=HumanPlayer(), player_two=HumanPlayer(), game_display=MockGameDisplay())
        self.board = self.game.board

    def test_game_is_over_message(self):
        GameDisplay.game_over()
        self.assertEqual(GameDisplay.message, "Game Over")

    def test_Player_O_sees_a_message_on_a_move_played_by_a_X(self):
        GameDisplay.chosen_spot("X", 4)
        self.assertEqual(
            GameDisplay.message,
            "Player with symbol X has played in spot 4",
            "The game board should display X at 4th position",
        )

    def test_Player_X_sees_a_message_on_a_move_played_by_a_O(self):
        GameDisplay.chosen_spot("O", 4)
        self.assertEqual(
            GameDisplay.message,
            "Player with symbol O has played in spot 4",
            "The game board should display O at 4th position",
        )

    def test_when_Player_X_wins_a_message_to_announce_the_winner_is_shown_to_the_screen(self):
        GameDisplay.winner("X")
        self.assertEqual(GameDisplay.message, "Player with symbol X won!", "The game should announce X as the winner")

    def test_when_Player_O_wins_a_message_to_announce_the_winner_is_shown_to_the_screen(self):
        GameDisplay.winner("O")
        self.assertEqual(GameDisplay.message, "Player with symbol O won!", "The game should announce O as the winner")

    def test_GameDisplay_tie_set_message_to_it_is_a_tie(self):
        GameDisplay.tie()
        self.assertEqual(GameDisplay.message, "It's a tie!", "The game should display there is a tie")

    def test_GameDisplay_game_types_asks_players_to_choose_type_of_game(self):
        GameDisplay.game_types()
        self.assertEqual(
            GameDisplay.message,
            "1. Human Vs Human\n2. Human Vs Computer",
            "The game should display an option to choose a game type",
        )

    def test_GameDisplay_prompt_spot_with_available_spots_a_player_can_choose_from(self):
        available_spots = ["4", "5"]
        GameDisplay.prompt_spot(available_spots)
        self.assertEqual(
            GameDisplay.message, "Choose one of these spots [4, 5]:", "The game should display the available spots"
        )

    def test_GameDisplay_prompt_first_player_asks_who_should_should_go_first(self):
        GameDisplay.prompt_first_player()
        self.assertEqual(
            GameDisplay.message,
            "Choose symbol, X or O?",
            "The game should give user a chance to pick who should go first",
        )

    def test_GameDisplay_get_board_size_asks_board_size(self):
        size = MockGameDisplay.get_board_size(MockGameDisplay)
        self.assertEqual(MockGameDisplay.message, "What board size you want to play?")
        self.assertEqual(self.board.size, size)


if __name__ == "__main__":
    unittest.main()
