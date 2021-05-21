import unittest
from game_session import GameSession
import core
from core.game_type import HumanVsHuman

class TestGameSession(unittest.TestCase):
   def setUp(self):
     self.game_session: GameSession = GameSession()
     self.game: core.Game = core.Game()
     self.humanPlayer = HumanVsHuman()

   def test_when_first_player_is_O_player_one_symbol_should_be_O(self):
      self.game_session.first_player = "O"
      self.game_session.handle_human_players_symbols()
      self.assertEqual(self.game_session.human_vs_human.playerOne.symbol, "O", "If the first player is O, player one symbol should be O")
      self.assertEqual(self.game_session.human_vs_human.playerTwo.symbol, "X", "If the first player is X, player one symbol should be X")
   
   def test_when_first_player_is_X_player_one_symbol_should_be_X(self):
      self.game_session.first_player = "X"
      self.game_session.handle_human_players_symbols()
      self.assertEqual(self.game_session.human_vs_human.playerOne.symbol, "X", "If the first player is X, player one symbol should be X")
      self.assertEqual(self.game_session.human_vs_human.playerTwo.symbol, "O", "If the first player is O, player one symbol should be O")

   def test_if_first_player_X_current_player_symbol_should_be_X_when_game_starts(self):
      first_player = "X"
      self.game.current_player_symbol = first_player
      self.game_session.handle_human_players_symbols()
      self.assertEqual(self.game.current_player_symbol, "X", "If first player is X, current player symbol should be X")
