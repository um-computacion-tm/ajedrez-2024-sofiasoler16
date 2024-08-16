import unittest

from game.piece import Rook, Pawn, Knight, Bishop, Queen, King
from game.board import Board
from game.chess import Chess

## Porque mi codeClimate me verifica el codigo de los tests?

class TestChess(unittest.TestCase):
    def setUp(self):
        self.chess = Chess()

    def test_chess_init(self):
        self.assertEqual(self.chess.__turn__, "WHITE")

    def test_change_turn(self):
        self.assertEqual(self.chess.__turn__, "WHITE")

    def test_turn_change(self):
        self.chess.change_turn()
        self.assertEqual(self.chess.__turn__, "BLACK")
        self.chess.change_turn()
        self.assertEqual(self.chess.__turn__, "WHITE")


    def test_move_piece(self):
        self.chess.move(7, 0, 6, 0)
        
        self.assertEqual(self.chess.__board__.get_piece(7, 0), "No piece")

        self.assertEqual(self.chess.__turn__, "BLACK")

    def test_move_no_piece(self):


        self.assertEqual(self.chess.__board__.get_piece(4, 4), "No piece")
        self.assertEqual(self.chess.__board__.get_piece(3, 3), "No piece")

        self.assertEqual(self.chess.__turn__, "WHITE")


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_init_board(self):
        self.assertEqual(self.board.__positions__[0][0].__type__, "ROOK")
        

    def test_get_piece_empty(self):
        self.assertEqual(self.board.get_piece(3, 3), "No piece")

    def test_move_piece(self):
        self.board.move_piece(0, 0, 0, 1)
        

        self.assertEqual(self.board.get_piece(0, 1), ({'ROOK'}, {'BLACK'}))

        self.assertEqual(self.board.get_piece(0, 0), "No piece")

    def test_move_piece_no_piece(self):

        result = self.board.move_piece(3, 3, 4, 4)


        self.assertEqual(result, "No piece to move")

        self.assertEqual(self.board.get_piece(3, 3), "No piece")
        self.assertEqual(self.board.get_piece(4, 4), "No piece")



class TestRook(unittest.TestCase):
    def test_rook_init(self):
        rook = Rook("BLACK")
        self.assertEqual(rook.__color__, "BLACK")
        self.assertEqual(rook.__type__, "ROOK")

    def test_pawn_init(self):
        pawn = Pawn("WHITE")
        self.assertEqual(pawn.__color__, "WHITE")
        self.assertEqual(pawn.__type__, "PAWN")

    def test_knight_init(self):
        knight = Knight("WHITE")
        self.assertEqual(knight.__color__, "WHITE")
        self.assertEqual(knight.__type__, "KNIGHT")

    def test_bishop_init(self):
        bishop = Bishop("WHITE")
        self.assertEqual(bishop.__color__, "WHITE")
        self.assertEqual(bishop.__type__, "BISHOP")

    def test_queen_init(self):
        queen = Queen("WHITE")
        self.assertEqual(queen.__color__, "WHITE")
        self.assertEqual(queen.__type__, "QUEEN")

    def test_king_init(self):
        king = King("WHITE")
        self.assertEqual(king.__color__, "WHITE")
        self.assertEqual(king.__type__, "KING")



if __name__ == '__main__':
    unittest.main()
