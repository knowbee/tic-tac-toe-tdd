from core import Game, GameDisplay, Board
from core.player import HumanPlayer, BotPlayer


class HumanVsComputer:
    def __init__(self, game: Game):
        # super().__init__()
        self.game = game
        self.player_one = HumanPlayer()
        self.player_two = BotPlayer()
