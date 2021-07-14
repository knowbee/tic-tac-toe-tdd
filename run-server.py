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
    response.headers.add("Access-Control-Allow-Origin", "https://c167ed55b573.ngrok.io")
    response.headers.add("Access-Control-Allow-Headers", "withCredentials, content-type")

    return response


@app.route("/")
def home():
    return jsonify({"message": "Welcome"})


@app.route("/play", methods=["POST"])
def play():
    response = Response("Setting a cookie")
    response = jsonify({"message": "this is the message"})
    response.set_cookie("board", value="a_cookie", max_age=1000, httponly=True)
    return response
    # game: Game = Game(request.json["first_player"], request.json["board_size"], request.json["move"])
    # game.play()
    # return jsonify({"finished": game.is_finished(), "winner": game.winner(), "board": list(game.board.grid)})


if __name__ == "__main__":
    app.run(debug=True)
