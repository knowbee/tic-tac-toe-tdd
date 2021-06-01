class GameState:
    def finished(self, board):
        return board.is_win() or self.tie(board)

    def is_winning_combination(self, combination: list, grid: list) -> bool:
        first_choice = grid[combination[0]]
        second_choice = grid[combination[1]]
        third_choice = grid[combination[2]]
        return first_choice == second_choice == third_choice

    def get_winner(self, board) -> str:
        for combination in board.get_all_combinations():
            if board.has_unique_elements(combination):
                return combination[0]
        return None

    def tie(self, board):
        return len([s for s in board.grid if s == "X" or s == "O"]) == 9
