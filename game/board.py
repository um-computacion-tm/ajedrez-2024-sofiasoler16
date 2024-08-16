from game.piece import Rook, Pawn

class Board:
    def __init__(self): #Asi inicia el tablero
        self.__positions__ = []
        for _ in range(8):
            col = []
            for _ in range(8):
                col.append(None)
            self.__positions__.append(col)

        self.__positions__[0][0] = Rook("BLACK") #"Rook Black"
        self.__positions__[0][7] = Rook("BLACK") #"Rook Black"
        self.__positions__[7][7] = Rook("WHITE") #"Rook White"
        self.__positions__[7][0] = Rook("WHITE") #"Rook White"

        self.__positions__[1][0] = Pawn("BLACK") #"PawnBlack"
        self.__positions__[1][2] = Pawn("BLACK") #"PawnBlack"
        self.__positions__[1][3] = Pawn("BLACK") #"PawnBlack"
        self.__positions__[1][4] = Pawn("BLACK") #"PawnBlack"
        self.__positions__[1][5] = Pawn("BLACK") #"PawnBlack"
        self.__positions__[1][6] = Pawn("BLACK") #"PawnBlack"
        self.__positions__[1][7] = Pawn("BLACK") #"PawnBlack"
        self.__positions__[6][1] = Pawn("WHITE") #"PawnWhite"
        self.__positions__[6][2] = Pawn("WHITE") #"PawnWhite"
        self.__positions__[6][3] = Pawn("WHITE") #"PawnWhite"
        self.__positions__[6][4] = Pawn("WHITE") #"PawnWhite"
        self.__positions__[6][5] = Pawn("WHITE") #"PawnWhite"
        self.__positions__[6][6] = Pawn("WHITE") #"PawnWhite"
        self.__positions__[6][7] = Pawn("WHITE") #"PawnWhite"
    
    def get_piece(self, row, col):
        piece = self.__positions__[row][col]
        if piece is None:
            return "No piece"
        return ("La pieza de esa posicion es: ", {piece.__type__}, {piece.__color__})
    
    def move_piece(self, from_row, from_col, to_row, to_col):
        piece = self.__positions__[from_row][from_col]

        if piece is None:
            print("No piece to move")
            return "No piece to move"

        self.__positions__[to_row][to_col] = piece

        self.__positions__[from_row][from_col] = None

        print(f"Moved piece from: ", {from_row}, {from_col}, "to: ", {to_row}, {to_col})
    
# board = Board()
# print(board.get_piece(0,0))
# print(board.get_piece(7,0))