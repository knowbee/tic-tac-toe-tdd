import random
from .player import Player
from core import GameDisplay, Board

class BotPlayer(Player):
  def __init__(self):
    super().__init__()

  def play(self, board):
    spot = int(self.get_random_available_spot(board))
    board.grid[spot] = self.symbol
    return spot
  
  def get_random_available_spot(self, board: Board) -> int:
    available_spot = board.get_available_spots()
    return random.choice(available_spot)
