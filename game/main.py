from game.chess import Chess
from game.board import Board

def main():
    chess = Chess() 
    #board = Board() #No se usa porque si creo un board aca esoy inhiendo al otro board, estoy como creando un board nuevo que no le he movido ninguna pieza
    try:
        from_row = int(input("From row: "))
        from_col = int(input("From col: "))
        print("The piece you have choosen is: ",chess.__board__.get_piece(from_row, from_col))
        to_row = int(input("To row: "))
        to_col = int(input("To col: "))

        chess.move(from_row, from_col,to_row,to_col)

        print("La pieza que quedo en la posicion es: ", chess.__board__.get_piece(from_row, from_col))

        print("La pieza que esta en la nueva posicion es: ", chess.__board__.get_piece(to_row, to_col))

    except Exception as e:
        print("error")
            

main()
