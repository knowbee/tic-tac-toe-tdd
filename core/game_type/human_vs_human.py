from core.player import HumanPlayer
from cli.game import Game
from cli.game_display import GameDisplay


class HumanVsHuman:
    def __init__(self, game: Game):
        self.game = game
        self.player_one = HumanPlayer()
        self.player_two = HumanPlayer()
