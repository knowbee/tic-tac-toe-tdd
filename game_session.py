from core.game_type import HumanVsHuman
from core import Game, GameDisplay


class GameSession:
    def __init__(self, human_vs_human: HumanVsHuman, game_diplay: GameDisplay):
        self.human_vs_human = human_vs_human
        self.game_display: GameDisplay = game_diplay

    def get_match(self):
        first_player: str = self.game_display.get_first_player()
        self.set_game_players(first_player)

        if self.game_display.get_game_type() == 0:
            return self.human_vs_human

    def set_game_players(self, first_player: str) -> Game:
        self.set_player_symbols(first_player)
        self._initiate_current_player_symbol(first_player)

    def set_player_symbols(self, first_player: str) -> None:
        if first_player == "X":
            self.human_vs_human.playerTwo.symbol = "O"
            self.human_vs_human.playerOne.symbol = "X"
        else:
            self.human_vs_human.playerTwo.symbol = "X"
            self.human_vs_human.playerOne.symbol = "O"

    def _initiate_current_player_symbol(self, first_player: str) -> None:
        self.human_vs_human.current_player_symbol = first_player


if __name__ == "__main__":
    game_session = GameSession(HumanVsHuman(), GameDisplay)
    match = game_session.get_match()
    match.play()
