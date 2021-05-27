from core.game_type import HumanVsHuman, HumanVsComputer
from core import Game, GameDisplay

class GameSession:
    def __init__(self, human_vs_human: HumanVsHuman, human_vs_computer: HumanVsComputer, game_display: GameDisplay):
        self.human_vs_human = human_vs_human
        self.human_vs_computer = human_vs_computer
        self.game_display: GameDisplay = game_display

    def get_match(self):
        if self.game_display.get_game_type() == 0:
            first_player: str = self.game_display.get_first_player()
            self.human_vs_human.set_game_players(first_player)
            return self.human_vs_human
        else:
            first_player: str = self.game_display.get_first_player()
            self.human_vs_computer.set_game_players(first_player)
            return self.human_vs_computer

if __name__ == "__main__":
    game_session = GameSession(HumanVsHuman(), HumanVsComputer(),  GameDisplay)
    match = game_session.get_match()
    match.play()
