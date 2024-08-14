from game.rook import Rook, Pawn

class Board:
    def __init__(self):
        self.__positions__ = []
        for _ in range(8):
            col = []
            for _ in range(8):
                col.append(None)
            self.positions.append(col)

        self.positions[0][0] = Rook("BLACK") #"Rook Black"
        self.positions[0][7] = Rook("BLACK") #"Rook Black"
        self.positions[7][7] = Rook("WHITE") #"Rook White"
        self.positions[7][0] = Rook("WHITE") #"Rook White"

        self.positions[1][0] = Pawn("BLACK") #"PawnBlack"
