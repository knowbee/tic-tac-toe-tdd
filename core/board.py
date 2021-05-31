from typing import List, Any


class Board:
    def __init__(self):
        self.size = 3
        self.grid = list(range(self.size * self.size))
        # Hard-coded... Not scalable if we move to 4x4, 5x5, etc.
        self.win_combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    def get_available_spots(self):
        available_spots = [str(s) for s in self.grid if s != "X" and s != "O"]
        return available_spots

    def is_empty(self):
        return len(self.get_available_spots()) == 9

    def reset(self):
        self.grid = list(range(9))

    def set_spot(self, spot: int, symbol: str) -> None:
        self.grid[spot] = symbol

    def is_win(self):
        all_combinations: List[list] = []

        all_rows: List[list] = self.get_all_rows()
        for row in all_rows:
            all_combinations.append(row)

        all_columns: List[list] = self.get_all_columns()
        for column in all_columns:
            all_combinations.append(column)

        all_diagonals: List[list] = [self.get_first_diagonal(), self.get_second_diagonal()]
        for diagonal in all_diagonals:
            all_combinations.append(diagonal)

        for combination in all_combinations:
            if self.has_unique_elements(combination):
                return True

        return False

    def get_all_rows(self) -> List[list]:
        all_rows: List[list] = self.generate_board()

        return [self.get_elements_at_spots(row) for row in all_rows]

    def get_all_columns(self) -> List[list]:
        all_columns: List[list] = []

        for i in range(self.size):  # i = 0
            column: List[int] = [i + j * self.size for j in range(self.size)]
            all_columns.append(self.get_elements_at_spots(column))
        return all_columns

    def generate_board(self) -> List[list]:
        # TODO Improve algorithm. Do not hardcode first row.
        first_row: List[int] = list(range(self.size))
        all_rows: List[list] = [first_row]

        for i in range(self.size - 1):
            row: List[int] = [e + self.size for e in all_rows[-1]]
            all_rows.append(row)

        return all_rows

    def get_first_diagonal(self) -> List[list]:
        first_diagonal: List[list] = []
        board: List[list] = self.generate_board()
        for i in range(self.size):
            first_diagonal.append(board[i][i])
        return self.get_elements_at_spots(first_diagonal)

    def get_second_diagonal(self) -> List[list]:
        second_diagonal: List[list] = []
        board: List[list] = self.generate_board()

        k: int = self.size - 1

        for i in range(self.size):
            second_diagonal.append(board[i][k])
            k -= 1
        return self.get_elements_at_spots(second_diagonal)

    def has_unique_elements(self, elements: List[int]) -> bool:
        return len(set(elements)) == 1

    def get_elements_at_spots(self, spots: List[int]) -> List[Any]:
        return [self.grid[s] for s in spots]
