
class Piece:
    def __init__(self, color):
        self.__color__ = color
        self.__type__ = None


class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.__type__ = "QUEEN"

    def permited_move(self, from_row, from_col, to_row, to_col, board):
        if to_row == from_row and to_col != from_col:
            return True
        elif to_col == from_col and to_row != from_row:
            return True
        elif abs(to_row - from_row) == abs(to_col - from_col): #Dice que hay dos bloques iguales, pero no los puedo cambiar porque los dos tienen el mismo movimiento :/
            return True
        else:
            return False
        
    def show(self):
        if self.__color__ == "WHITE":
            return "♛"
        else:
            return "♕"
        
class King(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.__type__ = "KING"

    def permited_move(self, from_row, from_col, to_row, to_col, board):
        if abs(from_row - to_row) <= 1 and abs(from_col - to_col) <= 1 and not (from_row == to_row and from_col == to_col):
            return True
        else: 
            return False
        
    def show(self):
        if self.__color__ == "WHITE":
            return "♚"
        else:
            return "♔"









