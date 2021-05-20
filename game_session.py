from core.game_type import HumanVsHuman
import core

class GameSession:
    def __init__(self):
        self.human_vs_human =  HumanVsHuman()

    @classmethod
    def get_first_player(cls):
        print("Who plays first? X or O")
        first_player = input()
        valid_input = ["O", "X"]
        if not first_player in valid_input:
            return cls.get_first_player(cls)
        else:
            return first_player

    def start(self):
        game_type = core.GameDisplay.get_game_type()
        first_player = self.get_first_player()
        if game_type == 0:
            self.human_vs_human.playerOne.symbol = first_player
            if first_player == "X":
                self.human_vs_human.playerTwo.symbol = "O"
            else:
                self.human_vs_human.playerTwo.symbol = "X"
            self.human_vs_human.play(first_player)
            return


if __name__ == "__main__":
    game = GameSession()
    game.start()
