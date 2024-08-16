import unittest

from game.piece import Rook, Pawn
from game.board import Board
from game.chess import Chess

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
        

        self.assertEqual(self.board.get_piece(0, 1), ('La pieza de esa posicion es: ', {'ROOK'}, {'BLACK'}))

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


# class TestMain(unittest.TestCase):
    # @patch('builtins.input', side_effect=[0, 0, 1, 0])
    # @patch('sys.stdout', new_callable=StringIO)  # Captura la salida estándar (print)
    # def test_main_valid_move(self, mock_stdout, mock_input):
    #     main()  # Ejecuta la función main()

    #     # Verifica la salida capturada
    #     output = mock_stdout.getvalue()
    #     self.assertIn("The piece you have choosen is: ROOK (BLACK)", output)

    # @patch('builtins.input', side_effect=[3, 3, 4, 4])
    # @patch('sys.stdout', new_callable=StringIO)  
    # def test_main_no_piece(self, mock_stdout, mock_input):
    #     main()  # Ejecuta la función main()

    #     # Verifica la salida capturada
    #     output = mock_stdout.getvalue()
    #     self.assertIn("The piece you have choosen is: No piece", output)





if __name__ == '__main__':
    unittest.main()
