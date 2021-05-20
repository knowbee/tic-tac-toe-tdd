import unittest
import core

class TestHandleTurns(unittest.TestCase):
    def setUp(self):
        self.handleTurns = core.HandleTurns()

    def test_has_current_player_symbol_property(self):
        self.assertEqual(self.handleTurns.currentPlayerSymbol, None, "It should return None when there is no current player")

    def test_sets_current_player_symbol(self):
        self.handleTurns.set_currentPlayerSymbol("O")
        self.assertEqual(self.handleTurns.currentPlayerSymbol, "O", "It should return O when current player is set to O")

    def test_triggered_new_turn_is_X(self):
        self.handleTurns.set_currentPlayerSymbol("O")
        self.handleTurns.change()
        self.assertEqual(self.handleTurns.currentPlayerSymbol, "X", "It should return X when current player is changed from O to X")

    def test_triggered_new_turn_is_O(self):
        self.handleTurns.set_currentPlayerSymbol("X")
        self.handleTurns.change()
        self.assertEqual(self.handleTurns.currentPlayerSymbol, "O", "It should return O when current player is changed from X to O")


if __name__ == "__main__":
    unittest.main()
