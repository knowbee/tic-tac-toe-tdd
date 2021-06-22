from flask import Flask, jsonify, render_template, request
from core import Board, GameState, Game, Symbols
from core.player import HumanPlayer, BotPlayer
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
game_state = GameState()
player = BotPlayer()


@app.route("/")
def home():
    return jsonify({"message": "Welcome"})


@app.route("/play", methods=["POST"])
def play():
    symbol = request.json["first_player"]
    player.symbol = Symbols[symbol].value
    board = Board(request.json["board_size"])
    board.grid = request.json["board"]
    player.play(board)
    is_finished: bool = game_state.finished(board)
    winner: Optional(bool) = game_state.get_winner(board)
    return jsonify({"finished": is_finished, "winner": winner, "board": list(board.grid)})


if __name__ == "__main__":
    app.run(debug=True)
