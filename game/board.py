from game.piece import Rook, Pawn, Knight, Bishop, Queen, King


#Que hacer con los permited_move, donde los pongo?
class NotPermitedMove(Exception):
    pass

class NotPieceToMove(Exception):
    pass



class Board:
    def __init__(self): #Asi inicia el tablero
        self.__positions__ = []
        for _ in range(8):
            col = []
            for _ in range(8):
                col.append(None)
            self.__positions__.append(col)

        #lugares rook
        self.__positions__[0][0] = Rook("BLACK") #"Rook Black"
        self.__positions__[0][7] = Rook("BLACK") #"Rook Black"
        self.__positions__[7][7] = Rook("WHITE") #"Rook White"
        self.__positions__[7][0] = Rook("WHITE") #"Rook White"

        #lugares pawn
        self.__positions__[1][0] = Pawn("BLACK") #"PawnBlack"
        self.__positions__[1][1] = Pawn("BLACK") #"PawnBlack"
        self.__positions__[1][2] = Pawn("BLACK") #"PawnBlack"
        self.__positions__[1][3] = Pawn("BLACK") #"PawnBlack"
        self.__positions__[1][4] = Pawn("BLACK") #"PawnBlack"
        self.__positions__[1][5] = Pawn("BLACK") #"PawnBlack"
        self.__positions__[1][6] = Pawn("BLACK") #"PawnBlack"
        self.__positions__[1][7] = Pawn("BLACK") #"PawnBlack"
        self.__positions__[6][0] = Pawn("WHITE") #"PawnWhite"
        self.__positions__[6][1] = Pawn("WHITE") #"PawnWhite"
        self.__positions__[6][2] = Pawn("WHITE") #"PawnWhite"
        self.__positions__[6][3] = Pawn("WHITE") #"PawnWhite"
        self.__positions__[6][4] = Pawn("WHITE") #"PawnWhite"
        self.__positions__[6][5] = Pawn("WHITE") #"PawnWhite"
        self.__positions__[6][6] = Pawn("WHITE") #"PawnWhite"
        self.__positions__[6][7] = Pawn("WHITE") #"PawnWhite"

        #lugares knight
        self.__positions__[0][1] = Knight("BLACK") #"KnightBlack"
        self.__positions__[0][6] = Knight("BLACK") #"KnightBlack"
        self.__positions__[7][1] = Knight("WHITE") #"KnightWhite"
        self.__positions__[7][6] = Knight("WHITE") #"KnightWhite"

        #lugares bushop
        self.__positions__[0][2] = Bishop("BLACK") #"BishopBlack"
        self.__positions__[0][5] = Bishop("BLACK") #"BishopBlack"
        self.__positions__[7][2] = Bishop("WHITE") #"BishopWhite"
        self.__positions__[7][5] = Bishop("WHITE") #"BishopWhite"

        #lugares queen
        self.__positions__[0][3] = Queen("BLACK") #"QueenBlack"
        self.__positions__[7][3] = Queen("WHITE") #"QueenWhite"


        #lugares king
        self.__positions__[0][4] = King("BLACK") #"KingBlack"
        self.__positions__[7][4] = King("WHITE") #"KingWhite"
    
    def get_piece(self, row, col):
        piece = self.__positions__[row][col]
        if piece is None:
            return "No piece"
        self.show_board
        return ({piece.__type__}, {piece.__color__})
    
    
    def permited_move(self, from_row, from_col, to_row, to_col):
        piece = self.__positions__[from_row][from_col]

        piece = self.__positions__[from_row][from_col]
        if piece is None:
            return False  # No hay pieza para mover
        return piece.permited_move(from_row, from_col, to_row, to_col, self)
    
    
    #Agregar que una pieza no se pueda mover a donde hay una pieza de su mismo color -- LISTO
    #Agregar que no permita mover una pieza del color que no es el turno -- LISTO

    def move_piece(self, from_row, from_col, to_row, to_col):
        try:
            piece = self.__positions__[from_row][from_col]
            
            if piece is None:
                raise NotPieceToMove("No piece to move")


            destination = self.__positions__[to_row][to_col]

            # Verificamos si la posición de destino tiene una pieza del mismo color
            if destination is not None and destination.__color__ == piece.__color__:
                self.show_board()
                raise NotPermitedMove("Cannot move to a position occupied by a piece of the same color")

            if self.permited_move(from_row, from_col, to_row, to_col) == False:
                self.show_board()
                raise NotPermitedMove("The piece cannot be moved in this position")

            self.__positions__[to_row][to_col] = piece

            self.__positions__[from_row][from_col] = None

            print(f"Moved piece from: ", {from_row}, {from_col}, "to: ", {to_row}, {to_col})

            self.show_board()

    #Hacer que cuando se equivoca en el turno, se le vuelva a pedir repetir el turno

        except NotPieceToMove as e:
            print("Error:", e)
            return str(e)
        except NotPermitedMove as e:
            print("Error:", e)
            return str(e)
        except Exception as e:
            print("Error:", e)
            return "Error"
    
    def show_board(self):

        print("    ", end="")
        for col in range(8):
            print(f"    {col} ", end="")
        print() 

        for row in range(8):
            print(f" {row} |", end="")  

            for col in range(8):
                piece = self.__positions__[row][col]
                if piece is None:
                    print("    ", end=" |")  # Espacio en blanco si no hay pieza
                else:
                    # print(f" {piece.__type__[0]}{piece.__color__[0]} ", end=" |")  # Muestra inicial del tipo y color de la pieza
                    print(" ", piece.show()," ",  end="|")  # Muestra inicial del tipo y color de la pieza
            print()
            print("    " + "------" * 8 + "")  # Línea separadora entre filas

# board = Board()
# board.show_board()
# print(board.get_piece(0,0))
# print(board.get_piece(7,0))
 