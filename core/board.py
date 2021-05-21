class Board:
    def __init__(self):
        self.grid = list(range(9))
        self.win_combinations = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

    def get_available_spots(self):
        available_spots = [str(s) for s in self.grid if s != "X" and s != "O"]
        return available_spots

    def is_empty(self):
        return len(self.get_available_spots()) == 9
        
    def reset(self):
        self.grid = list(range(9))
