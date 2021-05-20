from core.player import HumanPlayer
import core

class HumanVsHuman(core.Game):
    def __init__(self):
        super().__init__()
        self.playerOne = HumanPlayer()
        self.playerTwo = HumanPlayer()
