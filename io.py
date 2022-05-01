# I/O for the chess engine

from cv2 import split
import GameEngine
import renderer

def print_board(board):
    count = 0
    print("  1  2  3  4  5  6  7  8")
    for row in board:
        count = count + 1
        print(f"{count}", end=" ")
        for col in row:
            print(col, end=" ")
        print("\n")

def main():
    print_board(boardy.get_board())
    renderer.draw_board(boardy.get_board())
    while True:
        if boardy.turn == "w":
            print("White's turn")
            move_is_invalid = True
            while move_is_invalid:
                moving_piece = input("Enter the piece you want to move in the style of (x,x) with a comma: ")
                destination = input("Enter the destination in the style of (x,x) with a comma: ")
                moving_piece_row = int(moving_piece.split(",")[0])-1
                moving_piece_col = int(moving_piece.split(",")[1])-1
                destination_row = int(destination.split(",")[0])-1
                destination_col = int(destination.split(",")[1])-1
                # Dectect if the values are between 1 and 8 inclusive
                if (moving_piece_row >= 0 and moving_piece_row <= 7) and (moving_piece_col >= 0 and moving_piece_col <= 7) and (destination_row >= 0 and destination_row <= 7) and (destination_col >= 0 and destination_col <= 7):
                    if boardy.is_move_valid(moving_piece_row, moving_piece_col, destination_row, destination_col):
                        move_is_invalid = False
                else:
                    print("Invalid move. Try again.")
            boardy.update_board(moving_piece_row,moving_piece_col,destination_row,destination_col)
            print("----------------------------")
            boardy.turn = "b"
            print_board(boardy.get_board())
        else:
            print("Black's turn")
            move_is_invalid = True
            while move_is_invalid:
                moving_piece = input("Enter the piece you want to move in the style of (x,x) with a comma: ")
                destination = input("Enter the destination in the style of (x,x) with a comma: ")
                moving_piece_row = int(moving_piece.split(",")[0])-1
                moving_piece_col = int(moving_piece.split(",")[1])-1
                destination_row = int(destination.split(",")[0])-1
                destination_col = int(destination.split(",")[1])-1
                if (moving_piece_row >= 0 and moving_piece_row <= 7) and (moving_piece_col >= 0 and moving_piece_col <= 7) and (destination_row >= 0 and destination_row <= 7) and (destination_col >= 0 and destination_col <= 7):
                    if boardy.is_move_valid(moving_piece_row, moving_piece_col, destination_row, destination_col):
                        move_is_invalid = False
                else:
                    print("Invalid move. Try again.")
            boardy.update_board(moving_piece_row,moving_piece_col,destination_row,destination_col)
            print("----------------------------")
            boardy.turn = "w"
            print_board(boardy.get_board())
    print("Game over")

boardy = GameEngine.GameState()

main()