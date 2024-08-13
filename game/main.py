from game.chess import Chess

class Main():
    def main():
        chess = Chess()
        try:
            from_row = int(input("From row: "))
            from_col = int(input("From col: "))
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


if __name__ == "__main__":
    main()