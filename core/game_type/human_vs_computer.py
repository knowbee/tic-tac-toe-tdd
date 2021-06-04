from core import Game, GameDisplay, Board
from core.player import HumanPlayer, BotPlayer


class HumanVsComputer(Game):
    def __init__(self):
        super().__init__()
        self.player_one = HumanPlayer()
        self.player_two = BotPlayer()
