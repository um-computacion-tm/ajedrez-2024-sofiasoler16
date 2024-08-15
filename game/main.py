from game.chess import Chess
from game.board import Board

def main():
    chess = Chess()
    board = Board()
    try:
        from_row = int(input("From row: "))
        from_col = int(input("From col: "))
        print("The piece you have choosen is: ",board.get_piece(from_row, from_col))
        to_row = int(input("To row: "))
        to_col = int(input("To col: "))
    except Exception as e:
        print("error")
            
    chess.move(
        from_row,
        from_col,
        to_row,
        to_col,
    )


main()
