from core import Game, GameDisplay
from core.player import HumanPlayer, BotPlayer


class HumanVsComputer(Game):
    def __init__(self):
        super().__init__(size=GameDisplay.get_board_size())
        self.player_one = HumanPlayer()
        self.player_two = BotPlayer()
