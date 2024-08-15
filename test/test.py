import unittest

from unittest.mock import patch
from io import StringIO

from game.rook import Rook, Pawn
from game.board import Board
from game.chess import Chess
from game.main import main

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

class TestBoard(unittest.TestCase):
    def test_board_init(self):
        # Test that Rooks are correctly placed
        board = Board()
        self.assertEqual(board.get_piece(0, 0), "ROOK (BLACK)")
        self.assertEqual(board.get_piece(7, 0), "ROOK (WHITE)")
        
        # Test that Pawns are correctly placed
        self.assertEqual(board.get_piece(1, 0), "PAWN (BLACK)")
        self.assertEqual(board.get_piece(6, 1), "PAWN (WHITE)")
        
        # Test an empty square
        self.assertEqual(board.get_piece(4, 4), "No piece")

class TestRook(unittest.TestCase):
    def test_rook_init(self):
        rook = Rook("BLACK")
        self.assertEqual(rook.__color__, "BLACK")
        self.assertEqual(rook.__type__, "ROOK")

    def test_pawn_init(self):
        pawn = Pawn("WHITE")
        self.assertEqual(pawn.__color__, "WHITE")
        self.assertEqual(pawn.__type__, "PAWN")


class TestMain(unittest.TestCase):
    @patch('builtins.input', side_effect=[0, 0, 1, 0])
    @patch('sys.stdout', new_callable=StringIO)  # Captura la salida estándar (print)
    def test_main_valid_move(self, mock_stdout, mock_input):
        main()  # Ejecuta la función main()

        # Verifica la salida capturada
        output = mock_stdout.getvalue()
        self.assertIn("The piece you have choosen is: ROOK (BLACK)", output)

    @patch('builtins.input', side_effect=[3, 3, 4, 4])
    @patch('sys.stdout', new_callable=StringIO)  
    def test_main_no_piece(self, mock_stdout, mock_input):
        main()  # Ejecuta la función main()

        # Verifica la salida capturada
        output = mock_stdout.getvalue()
        self.assertIn("The piece you have choosen is: No piece", output)





if __name__ == '__main__':
    unittest.main()
