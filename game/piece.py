
class Piece:
    def __init__(self, color):
        self.__color__ = color
        self.__type__ = None



class Rook(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.__type__ = "ROOK" 

    def permited_move(self, from_row, from_col, to_row, to_col, board):
        if to_row == from_row and to_col != from_col:
            return True
        elif to_col == from_col and to_row != from_row:
            return True
        return False
    
    def show(self):
        if self.__color__ == "WHITE":
            return "♖"
        else:
            return "♜"

class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.__type__ = "PAWN"

    def permited_move(self, from_row, from_col, to_row, to_col, board):
        direction = -1 if self.__color__ == "WHITE" else 1
        if to_col == from_col:  # Movimiento hacia adelante
            if (to_row - from_row) == direction and board.get_piece(to_row, to_col) == "No piece":
                return True
            if (from_row == 6 and self.__color__ == "WHITE") or (from_row == 1 and self.__color__ == "BLACK"):
                if (to_row - from_row) == 2 * direction and board.get_piece(to_row, to_col) == "No piece":
                    return True
        if abs(to_col - from_col) == 1 and (to_row - from_row) == direction:
            destination_piece = board.get_piece(to_row, to_col)
            if destination_piece != "No piece" and destination_piece[1] != self.__color__:
                return True
        return False
    
    def show(self):
        if self.__color__ == "WHITE":
            return "♙"
        else:
            return "♟"


class Knight(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.__type__ = "KNIGHT"

    def permited_move(self, from_row, from_col, to_row, to_col, board):
        valid_moves = [
            (2, 1), (2, -1), (-2, 1), (-2, -1),
            (1, 2), (1, -2), (-1, 2), (-1, -2)]
        return (to_row - from_row, to_col - from_col) in valid_moves
    
    def show(self):
        if self.__color__ == "WHITE":
            return "♘"
        else:
            return "♞" 


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
            return "♗"
        else:
            return "♝"

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
            return "♕"
        else:
            return "♛"

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
            return "♔"
        else:
            return "♚"
