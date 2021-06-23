from core.player import HumanPlayer
from core.player.symbols import Symbols
from cli.game_display import GameDisplay
from core.game_state import GameState


class Game:
    def __init__(
        self,
        player_one,
        player_two,
        game_display: GameDisplay = None,
        board=None,
        game_state: GameState = None,
    ):
        self.game_display = game_display
        self.board = board
        self.game_state = game_state
        self.current_player_symbol = None
        self.player_one = player_one
        self.player_two = player_two

    def play(self):
        self.game_display.show(self.board)
        self.start()
        self.game_display.show(self.board)
        self.game_display.game_over()

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
            spot = self.game_display.get_player_spot(self.board.get_available_spots())
            player.play(self.board, spot)
            self.game_display.chosen_spot(player.symbol, spot)
        else:
            spot = player.play(self.board)
            self.game_display.chosen_spot(player.symbol, spot)
        self.game_display.show(self.board)
        self.handle_turns()

    def end_game(self):
        if self.board.is_win():
            winnerSymbol = self.game_state.get_winner(self.board)
            self.game_display.winner(winnerSymbol)
        elif self.game_state.finished(self.board):
            self.game_display.tie()
