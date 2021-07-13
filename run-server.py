from flask import Flask, jsonify, render_template, request, Response
from flask_cors import CORS
import json
import os
from server.game import Game

app = Flask(__name__)
CORS(app)


@app.after_request
def middleware_for_response(response):
    response.headers.add("Access-Control-Allow-Credentials", "true")
    response.headers.add("Access-Control-Allow-Origins", "http://localhost:3000")
    return response


@app.route("/")
def home():
    return jsonify({"message": "Welcome"})


@app.route("/play", methods=["POST"])
def play():
    response = Response("Setting a cookie")
    response.set_cookie("board", "a_cookie", httponly=True)
    return response
    # game: Game = Game(request.json["first_player"], request.json["board_size"], request.json["move"])
    # game.play()
    # return jsonify({"finished": game.is_finished(), "winner": game.winner(), "board": list(game.board.grid)})


if __name__ == "__main__":
    app.run(debug=True)
