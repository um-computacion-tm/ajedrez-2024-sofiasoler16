from game.chess import Chess
from game.board import Board
from game.piece import Piece

class InvalidPosition(Exception):
    pass

class NotPieceToMove(Exception):
    pass

class Cli():
    def main(self):
        self.play()

    def verify_move(self, chess): #Verifica el color del movimeinto
        while True:
            from_row = int(input("From row: "))
            from_col = int(input("From col: "))
            
            print("The piece you have chosen is: ", chess.__board__.get_piece(from_row, from_col))
            
            # Intentamos mover la pieza si es del color correcto
            move_by_color = chess.move_correct_color(from_row, from_col)
            
            if move_by_color is None:  # Si no hay error, se seleccionó la pieza correcta
                return from_row, from_col
            elif move_by_color == "You can't move a piece that doesn't exist":
                print("You can't move a piece that doesn't exist")
            else:
                print(move_by_color)  # Si hay un error, se vuelve a pedir la pieza



    def play(self):
        chess = Chess() 
        #board = Board() #No se usa porque si creo un board aca esoy inhiendo al otro board, estoy como creando un board nuevo que no le he movido ninguna pieza
        a = "y"
        try:
            while a == "y":
                
                from_row, from_col = self.verify_move(chess)

                to_row = int(input("To row: "))
                to_col = int(input("To col: "))
                # while True:
                #         # Intentamos mover la pieza
                #     move_error = chess.move(from_row, from_col, to_row, to_col)
                    
                #     if move_error is None:
                #         break  # Si no hubo errores, rompemos el bucle y cambiamos de turno
                #     else:
                #         print(move_error)  # Si hubo un error, se muestra y se vuelve a pedir la entrada


                chess.move(from_row, from_col,to_row,to_col)
                print("La pieza que quedo en la posicion es: ", chess.__board__.get_piece(from_row, from_col))

                print("La pieza que esta en la nueva posicion es: ", chess.__board__.get_piece(to_row, to_col))
                
                a = input("Do you want to continue? (y/n): ")
                if a == "y":
                    chess.change_turn()
                    print("Es turno de: ", chess.__turn__)

        except Exception as e:
            print("error", e)
            return "error"
                
if __name__ == "__main__":
    cli = Cli()
    cli.play()