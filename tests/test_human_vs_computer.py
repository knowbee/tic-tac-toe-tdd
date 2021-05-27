import unittest
from core import Game, Board
from core.player import HumanPlayer, BotPlayer
from core.game_type import HumanVsComputer

class MockGameDiplay(object):
    def get_first_player(self) -> str:
        return 'X'

class TestHumanVsComputer(unittest.TestCase):
  def setUp(self):
    self.game_display = MockGameDiplay()
    self.game = HumanVsComputer()
    self.board = Board()

  def test_game_subclass(self):
    self.assertTrue(issubclass(HumanVsComputer, Game))

  def test_computer_inherits_play_method(self):
    self.assertIsNotNone(self.game.play)

  def test_computer_inherits_end_game_method(self):
    self.assertIsNotNone(self.game.end_game) 

  def test_computer_inherits_start_method(self):
    self.assertIsNotNone(self.game.start) 

  def test_game_has_player_one(self):
    self.assertIsNotNone(self.game.player_one) 

  def test_game_has_player_two(self):
      self.assertIsNotNone(self.game.player_two) 

  def test_player_one_is_human_player_instance(self):
    self.assertIsInstance(self.game.player_one, HumanPlayer) 

  def test_player_two_is_bot_player_instance(self):
      self.assertIsInstance(self.game.player_two, BotPlayer) 

  def test_is_win_returns_true_when_there_a_winner(self):
      self.game.board.grid = ["O", "1", "X",
                              "O", "X", "5",
                              "O", "7", "8"]
      is_a_win:bool = self.game.game_state.is_win(self.game.board)
      self.assertEqual(is_a_win, True,"It should return True when there is a winner" )
  
  def test_ends_game_when_symbol_O_wins(self):
      self.game.board.grid = ["O", "X", "X",
                              "O", "X", "O",
                              "O", "O", "X"]
      self.game.end_game()
      is_a_win:bool = self.game.game_state.is_win(self.game.board)
      self.assertEqual(is_a_win, True, "It should announce the player with symbol O as the player" )

  def test_returns_true_when_game_is_over_without_a_winner(self):
      self.game.board.grid = ["X", "O", "X",
                          "O", "X", "O",
                          "O", "X", "O"]
      is_a_tie:bool = self.game.game_state.tie(self.game.board)
      self.assertEqual(is_a_tie , True, "It should return True when there is a tie" )
  
  def test_bot_player_current_player_symbol_X(self):
      self.assertTrue(self.board.is_empty())

      player = BotPlayer()
      player.symbol = "X"
      self.game.handle_play(player)

      self.assertEqual(self.game.current_player_symbol, "X")

if __name__ == "__main__":
  unittest.main()