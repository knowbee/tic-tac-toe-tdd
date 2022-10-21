from core import GameDisplay, Board
from core.player import HumanPlayer, BotPlayer
from cli.game import Game


class HumanVsComputer:
    def __init__(self, game: Game):
        self.game = game
        self.player_one: HumanPlayer = HumanPlayer()
        self.player_two: BotPlayer = BotPlayer()
