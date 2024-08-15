
class Piece:
    def __init__(self, color):
        self.__color__ = color
        self.__type__ = None



class Rook(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.__type__ = "ROOK" 


class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.__type__ = "PAWN"
