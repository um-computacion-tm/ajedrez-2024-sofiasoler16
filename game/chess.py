from game.board import Board
from game.exceptions import InvalidPosition, NotPieceToMove

class Chess:
    def __init__(self):
        self.__board__ = Board()
        self.__turn__ = "WHITE"

# Falta hacer que si ingresa valor out of range, al ejecutar move, se vuelva a producir el bucle y no frene -- LISTO
# Preguntar por docker

    def move(self,from_row, from_col, to_row, to_col):

        piece = self.__board__.get_piece(from_row, from_col)

        # Validar que los valores estén dentro de los límites del tablero
        if not (0 <= to_row <= 7) or not (0 <= to_col <= 7):
            raise InvalidPosition("Invalid position. Please enter a value between 0 and 7.")

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

    # def change_pawn_for_other(self, from_row, from_col):
    #     piece_type = self.__board__.get_piece(from_row, from_col)
    #     piece_position = self.__board__.__positions__[from_row][from_col]

    #     if piece_type == "Pawn" and piece_type.__color__ == "WHITE":
    #         if from_row == 0:
    #             self.define_new_piece_white(from_row, from_col)
    #     else:
    #         if from_row == 7:
    #             self.define_new_piece_black(from_row, from_col)

    def change_pawn_for_other(self, from_row, from_col, to_row, to_col):
        destination = self.__board__.get_piece(to_row, to_col)  # Obtener la pieza en la posición final
        
        # Verificar si el peón es blanco y ha llegado a la fila 0
        if "PAWN" in destination[0] and "WHITE" in destination[1] and to_row == 0:
            if self.__board__.pieces_from_black_piece:  # Verificar si hay piezas disponibles
                self.define_new_piece_white(from_row, from_col, to_row, to_col)
            else:
                print("No hay piezas disponibles para reemplazar el peón blanco.")
        
        # Verificar si el peón es negro y ha llegado a la fila 7
        elif "PAWN" in destination[0] and "BLACK" in destination[1] and to_row == 7:
            if self.__board__.pieces_from_white_piece:  # Verificar si hay piezas disponibles
                self.define_new_piece_black(from_row, from_col, to_row, to_col)
            else:
                print("No hay piezas disponibles para reemplazar el peón negro.")


    def define_new_piece_black(self, from_row, from_col, to_row, to_col):
                print("Las piezas a elegir son: ", self.__board__.pieces_from_white)
                index = int(input("Enter the NUMBER of position in the list of piece you want to change: "))
                new_piece =self.__board__.pieces_from_white_piece[index]
                self.__board__.__positions__[to_row][to_col] = new_piece
                print("Pieza definida en la posicion es : ", new_piece.show())

                return new_piece
    
    def define_new_piece_white(self, from_row, from_col, to_row, to_col):
                print("Las piezas a elegir son: ", self.__board__.pieces_from_black)
                index = int(input("Enter the NUMBER of position in the list of piece you want to change: "))
                new_piece =self.__board__.pieces_from_black_piece[index]
                self.__board__.__positions__[to_row][to_col] = new_piece
                print("Pieza definida en la posicion es : ", new_piece.show())

                return new_piece
