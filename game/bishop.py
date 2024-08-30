from game.piece import Piece

class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.__type__ = "BISHOP"

    def permited_move(self, from_row, from_col, to_row, to_col, board):
        if abs(to_row - from_row) == abs(to_col - from_col): # :/  :?
            return True
        else:
            return False
        
    def show(self):
        if self.__color__ == "WHITE":
            return "♝"
        else:
            return "♗"