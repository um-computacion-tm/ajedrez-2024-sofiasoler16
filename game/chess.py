from game.board import Board
from game.exceptions import InvalidPosition, NotPieceToMove

class Chess:
    def __init__(self):
        self.__board__ = Board()
        self.__turn__ = "WHITE"

# Falta hacer que si ingresa valor out of range, al ejecutar move, se vuelva a producir el bucle y no frene
# Preguntar por docker

    def move(self,from_row, from_col, to_row, to_col):

        piece = self.__board__.get_piece(from_row, from_col)

        # Validar que los valores estén dentro de los límites del tablero
        if not (0 <= to_row <= 7) or not (0 <= to_col <= 7):
            raise InvalidPosition("Invalid position. Please enter a value between 0 and 7.")
        
        # self.__board__.move_piece(from_row, from_col, to_row, to_col)
        # print(self.__board__.move_piece(from_row, from_col, to_row, to_col))
        return ("Esto devuelve move: ", self.__board__.move_piece(from_row, from_col, to_row, to_col))
        
    def move_correct_color(self, from_row, from_col):

        piece = self.__board__.get_piece(from_row, from_col)
        if piece == "No piece":
            return "You can't move a piece that doesn't exist"
            
        # Desempacamos la tupla en tipo de pieza y color
        piece_type, piece_color = piece
        
        # Convertimos el conjunto del color a una lista y accedemos al primer elemento
        color = list(piece_color)[0]

        if color == self.__turn__:
            True
        else:
            #print("You can't move a piece that is not your color, your color is: ", self.__turn__, "You are trying to move: ", color)
            return "You can't move a piece that is not your color"

    def change_turn(self):
        if self.__turn__ == "WHITE":
            self.__turn__ = "BLACK"
        else:
            self.__turn__ = "WHITE"
