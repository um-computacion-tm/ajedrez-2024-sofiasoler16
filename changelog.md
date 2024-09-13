# Changelog
# Sofia Soler

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog],
and this project adheres to [Semantic Versioning].

#--------------Tercer Sprint----------------

## [0.30] - 12-9-24
Created function permited_move_diagonal and permited_move_orthogonal in piece class to avoid repetition


#--------------Segundo Sprint----------------(11 commits)
## [0.295] - 10-9-24
FIxed position of show_board from board to chess

## [0.29] - 9-9-24
Added function eat_piece to board

## [0.28] - 8-9-24
Fixed error with the movement of the Knight and Added classes king and queen

## [0.27] - 6-9-24
Added function verify_color to cli

## [0.26] - 5-9-24
Added the possibility of continue the same turn if the player enters an invalid movement

## [0.25] - 4-9-24
Fixed error for Raise exception in move_piece try and except.

## [0.24] - 2-9-24
Added function validate_range_to to the cli

## [0.23] - 1-9-24
Added the possibility to continue with the same turn if a invalid position or letter is entered

## [0.22] - 31-8-24
Fixed compelexity for pawns 

## [0.21] - 30-8-24
Fixed the error for No piece to move and added a loop to ask for row and column again if error is raised

## [0.20] - 29-8-24
Separated the pieces classes and fixed Error for No piece to move


#--------------Primer Sprint----------------(12 commits)
## [0.195] - 27-8-24 (Martes)
Added the real pieces to the board

## [0.19] - 25-8-24
Added methods permited_move to the pieces specifically

## [0.18] - 24-8-24
Added the permited moves for pawns including the moves when the pawn can eat another piece

## [0.17] - 22-8-24
Added exceptions to move_piece method in board and added the error of moving a piece where there is already a piece of the same color

## [0.165] - 20-8-24 (Martes)
FIxed complexity metods in board and added tests

## [0.16] - 19-8-24
Added function move_correct_color to chess, it prohibits the move of a piece that is not your color

## [0.15] - 18-8-24
Added permited moves to queen, king and bishop

## [0.14] - 17-8-24
Added function permited_move to board for Knight and Rook

## [0.13] - 16-8-24
Added classes pieces knight, bishop, queen and king. Added function show_board and the possibility to end game in any moment

## [0.12] - 15-8-24
Added function move to chess, move_piece method to board, and fixed get_piece method

## [0.11] - 14-8-24
Added get_piece method to board, and the pawns on the board

## [0.10] - 13-8-24 (Martes)
Added classes board, chess, and rook