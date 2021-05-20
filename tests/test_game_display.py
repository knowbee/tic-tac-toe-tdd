import unittest
from cli import GameDisplay
from core.board import Board

class TestGameDisplay(unittest.TestCase):
    def setUp(self):
        self.board = Board()
    
    def test_game_board_is_displayed(self):
        board = ' 0 | 1 | 2 \n===+===+===\n 3 | 4 | 5 \n===+===+===\n 6 | 7 | 8 \n\n'
        self.assertEqual(board,
            " %s | %s | %s \n===+===+===\n %s | %s | %s \n===+===+===\n %s | %s | %s \n\n"
            % (
                self.board.grid[0],
                self.board.grid[1],
                self.board.grid[2],
                self.board.grid[3],
                self.board.grid[4],
                self.board.grid[5],
                self.board.grid[6],
                self.board.grid[7],
                self.board.grid[8],
            ),
        )

    def test_game_is_over_message(self):
        GameDisplay.game_over()
        self.assertEqual(GameDisplay.message, "Game Over")

    def test_O_sees_a_message_on_a_move_played_by_a_X(self):
        GameDisplay.chosen_spot("X", 4)
        self.assertEqual(
           GameDisplay.message, "Player with symbol X has played in spot 4"
        , "The game board should display X at 4th position")

    def test_X_sees_a_message_on_a_move_played_by_a_O(self):
        GameDisplay.chosen_spot("O", 4)
        self.assertEqual(
            GameDisplay.message, "Player with symbol O has played in spot 4"
        ,"The game board should display O at 4th position")

    def test_when_X_wins_a_message_to_announce_the_winner_is_shown_to_the_screen(self):
        GameDisplay.winner("X")
        self.assertEqual(GameDisplay.message, "Player with symbol X won!", "The game should announce X as the winner")

    def test_when_O_wins_a_message_to_announce_the_winner_is_shown_to_the_screen(self):
        GameDisplay.winner("O")
        self.assertEqual(GameDisplay.message, "Player with symbol O won!", "The game should announce O as the winner")

    def test_when_there_is_a_tie_a_message_shown_to_the_screen(self):
        GameDisplay.tie()
        self.assertEqual(GameDisplay.message, "It's a tie!", "The game should display there is a tie")

    def test_before_the_game_starts_players_choose_type_of_game(self):
        GameDisplay.game_types()
        self.assertEqual(GameDisplay.message, "1. Human Vs Human", "The game should display an option to choose a game type")

    def test_game_shows_available_spots_a_player_can_choose_from(self):
        available_spots = ["4", "5"]
        GameDisplay.prompt_spot(available_spots)
        self.assertEqual(GameDisplay.message, "Choose one of these spots [4, 5]:", "The game should display the available spots")

    def test_players_get_to_choose_who_should_should_go_first(self):
        GameDisplay.prompt_first_player()
        self.assertEqual(GameDisplay.message, "Who plays first, X or O?", "The game should give user a chance to pick who should go first")

if __name__ == "__main__":
    unittest.main()
