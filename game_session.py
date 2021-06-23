from core.player import HumanPlayer, BotPlayer
from cli import GameDisplay
from cli.game import Game
from core.board import Board
from core.game_state import GameState


class GameSession:
    def __init__(self, game_display: GameDisplay):
        self.game_display: GameDisplay = game_display

    @classmethod
    def get_game(cls, game_type: int):
        if game_type == 0:
            return Game(
                player_one=HumanPlayer(),
                player_two=HumanPlayer(),
                game_display=GameDisplay(),
                board=Board(GameDisplay.get_board_size()),
                game_state=GameState(),
            )
        else:
            return Game(
                player_one=HumanPlayer(),
                player_two=BotPlayer(),
                game_display=GameDisplay(),
                board=Board(GameDisplay.get_board_size()),
                game_state=GameState(),
            )

    def get_match(self):
        game_type: int = self.game_display.get_game_type(self.game_display)
        game = self.get_game(game_type)
        first_player: str = self.game_display.get_first_player()
        game.set_game_players(first_player)
        return game


if __name__ == "__main__":
    game_session: GameSession = GameSession(GameDisplay)
    match = game_session.get_match()
    match.play()
