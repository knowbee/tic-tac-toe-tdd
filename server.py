from flask import Flask, jsonify, render_template, request
from core import Board, GameState, Game, Symbols
from core.player import HumanPlayer, BotPlayer
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return jsonify({"message": "Welcome"})


@app.route("/play", methods=["POST"])
def play():
    game = Game(request.json["first_player"], request.json["board_size"], request.json["move"], request.remote_addr)
    game.play()
    game.clean_up()
    return jsonify({"finished": game.is_finished(), "winner": game.winner(), "board": list(game.board.grid)})


class Game:
    def __init__(self, symbol, board_size, move, ip_address):
        self.symbol = symbol
        self.move = move
        self.board = Board(board_size)
        self.game_state = GameState()
        self.bot_player = BotPlayer()
        self.unique_id = ip_address

    def play(self):
        self.set_up_symbol()
        self.create_db()

        self.human_play()
        self.bot_player.play(self.board)
        self.persist_state()

    def clean_up(self):
        if self.is_finished():
            os.remove(f"db/{self.unique_id}_current_state.json")

    def create_db(self):
        if not os.path.exists("db"):
            os.makedirs("db")

    def persist_state(self):
        with open(f"db/{self.unique_id}_current_state.json", "w") as current_state:
            json.dump(self.board.grid, current_state)

    def set_up_symbol(self):
        self.bot_player.symbol = Symbols[self.symbol].value

    def human_play(self):
        try:
            with open(f"db/{self.unique_id}_current_state.json") as f:
                data = json.load(f)
                self.board.grid = data
                if self.is_valid_move(self.board.grid):
                    self.board.set_spot(self.move, self.symbol)
        except Exception as e:
            self.board.set_spot(self.move, self.symbol)

    def is_valid_move(self, grid):
        return grid[self.move] != Symbols[self.symbol].name and grid[self.move] != Symbols[self.symbol].value

    def is_finished(self):
        return self.game_state.finished(self.board)

    def winner(self):
        return self.game_state.get_winner(self.board)


if __name__ == "__main__":
    app.run(debug=True)
