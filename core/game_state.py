from typing import Union


class GameState:
    def finished(self, board) -> bool:
        return board.is_win() or self.tie(board)

    def is_winning_combination(self, combination: list, grid: list) -> bool:
        first_choice = grid[combination[0]]
        second_choice = grid[combination[1]]
        third_choice = grid[combination[2]]
        return first_choice == second_choice == third_choice

    def get_winner(self, board) -> Union[int, None]:
        for combination in board.get_all_combinations():
            if board.has_unique_elements(combination):
                return combination[0]
        return None

    def tie(self, board) -> bool:
        return len([s for s in board.grid if s == "X" or s == "O"]) == board.size * board.size
