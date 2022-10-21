from typing import List, Any, Union


class GameDisplay:
    def __init__(self):
        self.message = None

    @classmethod
    def show(cls, board) -> None:
        formated_grid = cls.get_grid_with_nested_rows(board)
        for y in list(range(board.size)):
            row = ""
            for x in list(range(board.size)):
                if x != 0:
                    row += " | "
                row += "%1s" % formated_grid[y][x]
            print(row)

    @staticmethod
    def get_grid_with_nested_rows(board) -> List[Any]:
        grid: List[list] = []
        count = 0
        for i in range(board.size):
            row: List[Any] = board.grid[count : count + board.size]
            count += board.size
            grid.append(row)
        return grid

    @classmethod
    def game_over(cls) -> None:
        cls.message = "Game Over"
        print(cls.message)

    @classmethod
    def chosen_spot(cls, symbol: str, spot: int) -> None:
        cls.message = f"Player with symbol {symbol} has played in spot {spot}"
        print(cls.message)

    @classmethod
    def winner(cls, symbol: str) -> None:
        cls.message = f"Player with symbol {symbol} won!"
        print(cls.message)

    @classmethod
    def tie(cls) -> None:
        cls.message = "It's a tie!"
        print(cls.message)

    @classmethod
    def game_types(cls) -> List[str]:
        game_types: List[str] = ["1. Human Vs Human", "2. Human Vs Computer"]
        cls.message = "\n".join(game_types)
        print(cls.message)
        return game_types

    @classmethod
    def prompt_spot(cls, available_spots) -> None:
        cls.message = "Choose one of these spots [%s]:" % ", ".join(available_spots)
        print(cls.message)

    @classmethod
    def prompt_first_player(cls) -> None:
        cls.message = "Choose symbol, X or O?"
        print(cls.message)

    @classmethod
    def get_player_spot(cls, available_spots: List[int]) -> int:
        cls.prompt_spot(available_spots)
        spot: str = input()
        if cls.is_valid_spot(spot, available_spots):
            return cls.format_input(spot)
        return cls.get_player_spot(available_spots)

    @staticmethod
    def is_valid_spot(spot, available_spots: List[int]) -> bool:
        return spot in available_spots

    @staticmethod
    def format_input(spot: str) -> int:
        return int(spot)

    @classmethod
    def get_first_player(cls) -> str:
        cls.prompt_first_player()
        first_player: str = input()
        valid_input: List[str] = ["O", "X"]
        if first_player not in valid_input:
            return cls.get_first_player(cls)
        else:
            return first_player

    @classmethod
    def get_board_size(cls):
        cls.message = "What board size do you want to play?"
        print(cls.message)
        size = input()
        return cls.format_input(size)

    def get_game_type(self) -> int:
        game_types: List[str] = self.game_types()
        game_type: str = input()
        game_type_index: int = self.handle_game_type_input(game_type)
        if game_type_index == None or not game_types[game_type_index] in game_types:
            return self.get_game_type()
        else:
            return game_type_index

    @classmethod
    def handle_game_type_input(cls, game_type) -> Union[int, None]:
        if game_type == "1":
            return 0
        if game_type == "2":
            return 1
        return None
