from typing import List, Any


class Board:
    def __init__(self, size):
        self.size = size
        self.grid = list(range(size * size))

    def get_available_spots(self):
        available_spots = [str(s) for s in self.grid if s != "X" and s != "O"]
        return available_spots

    def is_empty(self):
        if self.size is not None:
            return len(self.get_available_spots()) == self.size ** 2

    def reset(self):
        self.grid = list(range(self.size ** 2))

    def set_spot(self, spot: int, symbol: str) -> None:
        self.grid[spot] = symbol

    def _add_new_combinations(self, new_combinations: List[list], all_combinations: List[list]) -> None:
        for combination in new_combinations:
            all_combinations.append(combination)

    def get_both_diagonals(self):
        return [self.top_left_to_bottom_right_diagonal(), self.bottom_left_to_top_right_diagonal()]

    def get_all_combinations(self) -> List[list]:
        all_combinations: List[list] = []
        self._add_new_combinations(self.get_all_rows(), all_combinations)
        self._add_new_combinations(self.get_all_columns(), all_combinations)
        self._add_new_combinations(self.get_both_diagonals(), all_combinations)
        return all_combinations

    def is_win(self) -> bool:
        all_combinations: List[list] = self.get_all_combinations()
        for combination in all_combinations:
            if self.has_unique_elements(combination):
                return True
        return False

    def get_expected_winning_spot(self) -> List[int]:
        all_combinations: List[list] = self.get_all_combinations()
        for combination in all_combinations:
            if self.has_almost_unique_elements(combination):
                return self.get_winning_spot(combination)

    def get_winning_spot(self, combination: List):
        winning_spot = [int(s) for s in combination if s != "X" and s != "O"][0]
        return winning_spot

    def get_all_rows(self) -> List[list]:
        all_rows: List[list] = self.generate_board()
        return [self.get_elements_at_spots(row) for row in all_rows]

    def get_all_columns(self) -> List[list]:
        all_columns: List[list] = []

        for i in range(self.size):
            column: List[int] = [i + j * self.size for j in range(self.size)]
            all_columns.append(self.get_elements_at_spots(column))
        return all_columns

    def generate_board(self) -> List[list]:
        size = self.size
        if size is None:
            size = 3

        first_row: List[int] = list(range(size))
        all_rows: List[list] = [first_row]
        for i in range(size - 1):
            row: List[int] = [e + size for e in all_rows[-1]]
            all_rows.append(row)
        return all_rows

    def top_left_to_bottom_right_diagonal(self) -> List[list]:
        first_diagonal: List[list] = []
        board: List[list] = self.generate_board()
        for i in range(self.size):
            first_diagonal.append(board[i][i])
        return self.get_elements_at_spots(first_diagonal)

    def bottom_left_to_top_right_diagonal(self) -> List[list]:
        second_diagonal: List[list] = []
        board: List[list] = self.generate_board()

        k: int = self.size - 1

        for i in range(self.size):
            second_diagonal.append(board[i][k])
            k -= 1
        return self.get_elements_at_spots(second_diagonal)

    def has_unique_elements(self, elements: List[int]) -> bool:
        return len(set(elements)) == 1

    def has_almost_unique_elements(self, elements: List[int]) -> bool:
        return len(set(elements)) == 2

    def get_elements_at_spots(self, spots: List[int]) -> List[Any]:
        return [self.grid[s] for s in spots]
