
class Piece:
    def __init__(self, color):
        self.__color__ = color
        self.__type__ = None


    def permited_move_diagonal(self, from_row, from_col, to_row, to_col, board):
        if abs(to_row - from_row) == abs(to_col - from_col): # :/  :?
            return True
        
    def permited_move_orthogonal(self, from_row, from_col, to_row, to_col, board):
        if to_row == from_row and to_col != from_col:
            return True
        elif to_col == from_col and to_row != from_row:
            return True






