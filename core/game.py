from core import GameState, Board, GameDisplay
from core.player import HumanPlayer
from core.player.symbols import Symbols


class Game:
    def __init__(self, player_one, player_two, game_display):
        self.game_display = GameDisplay
        self.board = Board(size=self.game_display.get_board_size())
        self.game_state = GameState()
        self.current_player_symbol = None
        self.player_one = player_one
        self.player_two = player_two

    def play(self):
        GameDisplay.show(self.board)
        self.start()
        GameDisplay.show(self.board)
        GameDisplay.game_over()

    def set_game_players(self, first_player: str):
        self._initiate_current_player_symbol(first_player)
        self.set_player_symbols(first_player)

    def set_player_symbols(self, first_player: str) -> None:
        if first_player == Symbols(first_player).name:
            self.player_two.symbol = Symbols(first_player).value
            self.player_one.symbol = Symbols(first_player).name
        else:
            self.player_two.symbol = Symbols(first_player).name
            self.player_one.symbol = Symbols(first_player).value

        print(self.player_one.symbol, self.player_two.symbol, self.current_player_symbol)

    def _initiate_current_player_symbol(self, first_player: str) -> None:
        self.current_player_symbol = first_player

    def handle_turns(self):
        if self.current_player_symbol == Symbols(self.current_player_symbol).name:
            self.current_player_symbol = Symbols(self.current_player_symbol).value
        else:
            self.current_player_symbol = Symbols(self.current_player_symbol).name

    def start(self):
        while not self.game_state.finished(self.board):
            if self.current_player_symbol == self.player_one.symbol:
                self.handle_play(self.player_one)
            else:
                self.handle_play(self.player_two)
        self.end_game()

    def handle_play(self, player):
        if isinstance(player, HumanPlayer):
            spot = GameDisplay.get_player_spot(self.board.get_available_spots())
            player.play(self.board, spot)
            GameDisplay.chosen_spot(player.symbol, spot)
        else:
            spot = player.play(self.board)
            GameDisplay.chosen_spot(player.symbol, spot)
        GameDisplay.show(self.board)
        self.handle_turns()

    def end_game(self):
        if self.board.is_win():
            winnerSymbol = self.game_state.get_winner(self.board)
            GameDisplay.winner(winnerSymbol)
        elif self.game_state.finished(self.board):
            GameDisplay.tie()
