import core
class Game:
    def __init__(self):
        self.board = core.Board()
        self.game_state = core.GameState()
        self.current_player_symbol = None
        self.playerOne = None
        self.playerTwo = None

    def play(self):
        core.GameDisplay.show(self.board)
        self.handle_turns()
        self.start()
        core.GameDisplay.show(self.board)
        core.GameDisplay.game_over()

    def handle_turns(self):
        if self.current_player_symbol == 'X':
            self.current_player_symbol = "O"
        else:
            self.current_player_symbol = "X"

    def start(self):
       while not self.game_state.finished(self.board):
           if(self.current_player_symbol == self.playerOne.symbol):
             self.handle_play(self.playerOne)
           else:
             self.handle_play(self.playerTwo)
       self.end_game()

    def handle_play(self, player):
        spot = core.GameDisplay.get_player_spot(self.board.get_available_spots())
        player.play(self.board, spot)
        core.GameDisplay.chosen_spot(player.symbol, spot)
        core.GameDisplay.show(self.board)
        self.handle_turns()

    def end_game(self):
        if (self.game_state.is_win(self.board)):
         winnerSymbol = self.game_state.get_winner(self.board)
         core.GameDisplay.winner(winnerSymbol)
        elif (self.game_state.finished(self.board)):
         core.GameDisplay.tie()