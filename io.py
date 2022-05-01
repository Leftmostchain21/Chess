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
    renderer.draw_board()
    renderer.load_Images()
    while True:
        if boardy.turn == "w":
            print("White's turn")
            move_is_invalid = True
            while move_is_invalid:
                renderer.draw_board()
                renderer.draw_pieces(boardy.get_board())
                moving_piece = renderer.get_events()
                moving_piece_row = moving_piece[0][0]
                moving_piece_col = moving_piece[0][1]
                destination_row = moving_piece[1][0]
                destination_col = moving_piece[1][1]
                # Dectect if the values are between 1 and 8 inclusive
                if (moving_piece_row >= 0 and moving_piece_row <= 7) and (moving_piece_col >= 0 and moving_piece_col <= 7) and (destination_row >= 0 and destination_row <= 7) and (destination_col >= 0 and destination_col <= 7):
                    if boardy.is_move_valid(moving_piece_row, moving_piece_col, destination_row, destination_col):
                        if boardy.get_item_from_board(moving_piece_row, moving_piece_col) == "Kw":
                            boardy.king_location_w = destination_row, destination_col
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
                renderer.draw_board()
                renderer.draw_pieces(boardy.get_board())
                moving_piece = renderer.get_events()
                moving_piece_row = moving_piece[0][0]
                moving_piece_col = moving_piece[0][1]
                destination_row = moving_piece[1][0]
                destination_col = moving_piece[1][1]                
                if (moving_piece_row >= 0 and moving_piece_row <= 7) and (moving_piece_col >= 0 and moving_piece_col <= 7) and (destination_row >= 0 and destination_row <= 7) and (destination_col >= 0 and destination_col <= 7):
                    if boardy.is_move_valid(moving_piece_row, moving_piece_col, destination_row, destination_col):
                        if boardy.get_item_from_board(moving_piece_row, moving_piece_col) == "Kb":
                            boardy.king_location_w = destination_row, destination_col
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