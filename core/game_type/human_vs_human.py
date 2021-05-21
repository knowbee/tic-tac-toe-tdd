from core.player import HumanPlayer
from core.game import Game
class HumanVsHuman(Game):
    def __init__(self):
        super().__init__()
        self.playerOne = HumanPlayer()
        self.playerTwo = HumanPlayer()
