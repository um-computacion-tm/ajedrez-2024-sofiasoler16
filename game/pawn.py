from game.piece import Piece

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
            return "♟"
        else:
            return "♙"
