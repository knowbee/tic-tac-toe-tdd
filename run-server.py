from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
import json
import os
from server.game import Game

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


if __name__ == "__main__":
    app.run(debug=True)
