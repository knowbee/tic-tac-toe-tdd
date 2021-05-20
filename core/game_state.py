class GameState:

  def finished(self, board):
      return self.is_win(board) or self.tie(board)

  def is_win(self, board) -> bool:
      for combination in board.win_combinations:
          if self.is_winning_combination(combination, board.grid): return True
      return False

  def is_winning_combination(self,combination: list, grid: list) -> bool:
      first_choice = grid[combination[0]]
      second_choice = grid[combination[1]]
      third_choice = grid[combination[2]]
      return first_choice == second_choice == third_choice

  def get_winner(self, board) -> str:
      for combination in board.win_combinations:
        if self.is_winning_combination(combination, board.grid):
            return board.grid[combination[0]]
      return None

  def tie(self, board):
    return len([s for s in board.grid if s == "X" or s == "O"]) == 9