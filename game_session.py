from core.game_type import HumanVsHuman
import core

class GameSession:
    def __init__(self):
        self.human_vs_human =  HumanVsHuman()
        self.game = core.Game()
        self.game_type = None
        self.first_player = None

    def start_game_session(self):
        self.handle_game_type()
        self.first_player: str = self.get_first_player()
        if self.game_type == 0:
            self.handle_human_players_symbols()
            self.human_vs_human.play()
            return
    
    def handle_game_type(self):
        self.game_type = core.GameDisplay.get_game_type()
        
    @classmethod
    def get_first_player(cls) -> str:
        print("Who plays first? X or O")
        first_player = input()
        valid_input = ["O", "X"]
        if not first_player in valid_input:
            return cls.get_first_player(cls)
        else:
            return first_player
    
    def handle_human_players_symbols(self):
        if self.first_player == "X":
            self.human_vs_human.playerTwo.symbol = "O"
            self.human_vs_human.playerOne.symbol = "X"
        else:
            self.human_vs_human.playerTwo.symbol = "X"
            self.human_vs_human.playerOne.symbol = "O"

if __name__ == "__main__":
    game = GameSession()
    game.start_game_session()
