# Game engine for the game chess

from operator import xor


class GameEngine:
    def __init__(self) -> None:
        pass

class GameState(GameEngine):
    def __init__(self):
        # A 2d array of pieces for the state of the board
        self.board = [
        ["Rb","Nb","Bb","Qb","Kb","Bb","Nb","Rb"],
        ["Pb","Pb","Pb","Pb","Pb","Pb","Pb","Pb"],
        ["  ","  ","  ","  ","  ","  ","  ","  "],
        ["  ","  ","  ","  ","  ","  ","  ","  "],
        ["  ","  ","  ","  ","  ","  ","  ","  "],
        ["  ","  ","  ","  ","  ","  ","  ","  "],
        ["Pw","Pw","Pw","Pw","Pw","Pw","Pw","Pw"],
        ["Rw","Nw","Bw","Qw","Kw","Bw","Nw","Rw"]]
        self.turn = "w"
        self.white_pieces = ["Pw","Pw","Pw","Pw","Pw","Pw","Pw","Pw","Rw","Nw","Bw","Qw","Kw","Bw","Nw","Rw"]
        self.black_pieces = ["Pb","Pb","Pb","Pb","Pb","Pb","Pb","Pb","Rb","Nb","Bb","Qb","Kb","Bb","Nb","Rb"]
        self.king_location_w = (7,4)
        self.king_location_b = (0,4)
        
    def get_board(self):
        return self.board

    def knight_move(self, row, col):
        # Check if the move is a valid knight move
        possible_moves = []
        for r,c in [(1,2),(2,1)]:
            for dr,dc in [(r,c),(r,-c),(-r,c),(-r,-c)]:
                if row+dr in range(0,8) and col+dc in range(0,8):
                    possible_moves.append((row+dr,col+dc))
        return possible_moves

    def bishop_move(self, og_row, og_col, row, col):
        # Check if the move is a valid bishop move
        possible_moves = []
        not_at_destination = True
        # Check in the vector direction of the bishop
        if row > og_row and col > og_col:
            while not_at_destination:
                possible_moves.append((row,col))
                row -= 1
                col -= 1
                if row == og_row and col == og_col:
                    not_at_destination = False

        elif row > og_row and col < og_col:
            while not_at_destination:
                possible_moves.append((row,col))
                row -= 1
                col += 1
                if row == og_row and col == og_col:
                    not_at_destination = False
        
        elif row < og_row and col > og_col:
            while not_at_destination:
                possible_moves.append((row,col))
                row += 1
                col -= 1
                if row == og_row and col == og_col:
                    not_at_destination = False
        
        elif row < og_row and col < og_col:
            while not_at_destination:
                possible_moves.append((row,col))
                row += 1
                col += 1
                if row == og_row and col == og_col:
                    not_at_destination = False
            
        return possible_moves

    def queen_move(self, og_row, og_col, row, col):
        # Check if the move is a valid bishop move
        possible_moves = []
        not_at_destination = True
        # Check in the vector direction of the queen
        if row == og_row:
            if col > og_col:
                while not_at_destination:
                    possible_moves.append((row,col))
                    col -= 1
                    if col == og_col:
                        not_at_destination = False
            else:
                while not_at_destination:
                    possible_moves.append((row,col))
                    col += 1
                    if col == og_col:
                        not_at_destination = False            
        if col == og_col:
            if row > og_row:
                while not_at_destination:
                    possible_moves.append((row,col))
                    row -= 1
                    if row == og_row:
                        not_at_destination = False
            else:
                while not_at_destination:
                    possible_moves.append((row,col))
                    row += 1
                    if row == og_row:
                        not_at_destination = False
        else:
            if row > og_row and col > og_col:
                while not_at_destination:
                    possible_moves.append((row,col))
                    row -= 1
                    col -= 1
                    if row == og_row and col == og_col:
                        not_at_destination = False

            elif row > og_row and col < og_col:
                while not_at_destination:
                    possible_moves.append((row,col))
                    row -= 1
                    col += 1
                    if row == og_row and col == og_col:
                        not_at_destination = False
            
            elif row < og_row and col > og_col:
                while not_at_destination:
                    possible_moves.append((row,col))
                    row += 1
                    col -= 1
                    if row == og_row and col == og_col:
                        not_at_destination = False
            
            elif row < og_row and col < og_col:
                while not_at_destination:
                    possible_moves.append((row,col))
                    row += 1
                    col += 1
                    if row == og_row and col == og_col:
                        not_at_destination = False
            
        return possible_moves

    def king_move(self, og_row, og_col, row, col):
        # Check if the move is a valid king move
        possible_moves = []
        # Check if the move is a valid king move
        if row == og_row:
            if col > og_col:
                possible_moves.append((row,col))
            else:
                possible_moves.append((row,col))
        elif col == og_col:
            if row > og_row:
                possible_moves.append((row,col))
            else:
                possible_moves.append((row,col))
        else:
            if row > og_row and col > og_col:
                possible_moves.append((row,col))
            elif row > og_row and col < og_col:
                possible_moves.append((row,col))
            elif row < og_row and col > og_col:
                possible_moves.append((row,col))
            elif row < og_row and col < og_col:
                possible_moves.append((row,col))
        return possible_moves

    def pawn_move(self, og_row, og_col, row, col):
        piece = self.get_item_from_board(og_row, og_col)
        dying_piece = self.get_item_from_board(row, col)
        if piece[-1:] == "w":
            if og_row <= row:
                print("You cannot move a piece backwards!")
                return False
            if dying_piece != "  " and og_col == col:
                print("You cannot move into a space that is not empty!")
                return False
            # Check if the pawn is moving more than two spaces at the beginning
            if og_row == 6 and og_row - row > 2:
                print("You cannot move a pawn more than two spaces at the beginning!")
                return False
            # Check if the pawn is moving more than one space after the first move
            if og_row != 6 and og_row - row > 1:
                print("You cannot move a pawn more than one space after the first move!")
                return False
            # If the pawn is is moving more than 1 in both directions, return false, but it must account for the first move of potencially 2 places
            if (abs(row - og_row) > 1 and abs(col - og_col) > 1) and og_row == 6:
                print("You cannot move more than one space in both directions!")
                return False 

        if piece[-1:] == "b":
            if og_row >= row:
                print("You cannot move a piece backwards!")
                return False
            if dying_piece != "  " and og_col == col:
                print("You cannot move into a space that is not empty!")
                return False
            # Check if the pawn is moving more than two spaces at the beginning
            if og_row == 1 and row - og_row > 2:
                print("You cannot move a pawn more than two spaces at the beginning!")
                return False
            # Check if the pawn is moving more than one space after the first move
            if og_row != 1 and row - og_row > 1:
                print("You cannot move a pawn more than one space after the first move!")
                return False
            # If the pawn is is moving more than 1 in both directions, return false, but it must account for the first move of potencially 2 places
            if (abs(row - og_row) > 1 and abs(col - og_col) > 1) and og_row == 1:
                print("You cannot move more than one space in both directions!")
                return False  
                
        # If the pawn is moving diagonal 1 space, check if the space is empty
        # if og_col != col and abs(row - og_row) == 1:
        #     if dying_piece == "  ":
        #         print("You cannot move into a space that is not empty!")
        #         return False

    def is_in_check(self, row, col):
        # This will work by treating the king as a piece and checking if it can move to any of the other pieces
        # If it can, then it is in check
        # If it cannot, then it is not in check

        row = row - 1
        col = col - 1

        # First we check for knights
        possible_moves = []
        for r,c in [(1,2),(2,1)]:
            for dr,dc in [(r,c),(r,-c),(-r,c),(-r,-c)]:
                if row+dr in range(0,8) and col+dc in range(0,8):
                    possible_moves.append(((row+dr,col+dc),"N"))
        # Now we check for bishops
        for r,c in [(1,1),(1,-1),(-1,1),(-1,-1)]:
            for dr,dc in [(r,c),(r,-c),(-r,c),(-r,-c)]:
                if row+dr in range(0,8) and col+dc in range(0,8):
                    possible_moves.append(((row+dr,col+dc),"B"))
        # Now we check for rooks
        for r,c in [(1,0),(0,1),(-1,0),(0,-1)]:
            for dr,dc in [(r,c),(r,-c),(-r,c),(-r,-c)]:
                if row+dr in range(0,8) and col+dc in range(0,8):
                    possible_moves.append(((row+dr,col+dc),"R"))
        # Now we check for pawns
        if self.get_item_from_board(row, col)[-1:] == "w":
            if self.get_item_from_board(row-1, col-1):
                possible_moves.append(((row-1,col-1),"P"))
            if self.get_item_from_board(row-1, col+1):
                possible_moves.append(((row-1,col), "P"))
        if self.get_item_from_board(row, col)[-1:] == "b":
            if self.get_item_from_board(row+1, col-1):
                possible_moves.append(((row+1,col-1),"P"))
            if self.get_item_from_board(row+1, col+1):
                possible_moves.append(((row+1,col),"P"))
        # Now we check for kings
        for r,c in [(1,0),(0,1),(-1,0),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]:
            possible_moves.append(((row+r,col+c),"K"))

        # Now we check for queens
        for r,c in [(1,0),(0,1),(-1,0),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]:
            for dr,dc in [(r,c),(r,-c),(-r,c),(-r,-c)]:
                if row+dr in range(0,8) and col+dc in range(0,8):
                    possible_moves.append(((row+dr,col+dc),"Q"))
        return possible_moves

    def get_item_from_board(self, row, col):
        print(row, col)
        return self.board[row][col]

    def alternate_move(self):
        if self.turn == "w":
            self.turn = "b"
        else:
            self.turn = "w"

    def is_move_valid(self, og_row, og_col, row, col):
        piece = self.get_item_from_board(og_row, og_col)
        dying_piece = self.get_item_from_board(row, col)
        # Check if the move is valid
        print(self.is_in_check(self.king_location_w[0], self.king_location_w[1]))
        if self.turn == "w":
            attacking_possible_moves = self.is_in_check(self.king_location_w[0], self.king_location_w[1])
            for attempts in range(0, len(attacking_possible_moves)):
                row = attacking_possible_moves[attempts][0]
                col = attacking_possible_moves[attempts][1]
                print(row, col)
                if piece[-1:] != self.turn and self.get_item_from_board(row,col)[-1:] != " ":
                    print("You are in check!")
                    return False
        if self.turn == "b":
            if self.king_location_b in self.is_in_check(self.king_location_b[0], self.king_location_b[1]):
                print("You cannot move into check!")
                return False
        if piece[-1:] == dying_piece[-1:]:
            print("You cannot move a piece to the same color!")
            return False
        if piece == "  ":
            print("You cannot move an empty space!")
            return False
        if piece[-1:] != self.turn:
            print("You cannot move the opponents piece!")
            return False
        if piece[:1] == "P":
            if self.pawn_move(og_row, og_col, row, col) == False:
                return False       

        if piece[:1] == "R":
            if og_row != row and og_col != col:
                print("You cannot move a rook diagonally!")
                return False

            # Row check

            if og_row == row:
                total_hit_enemy_pieces = 0
                # Check if the rook is moving through a piece of its own color
                for i in range(min(og_col, col), max(og_col, col)):
                    # Check if the piece is a piece of the same color
                    if self.get_item_from_board(row, i)[-1:] == piece[-1:]:
                        if i != og_col:
                            print("You cannot move through a piece of the same color!")
                            return False                        
                    # Check if the player has gone through an enemy piece
                    if self.get_item_from_board(row, i)[-1:] != piece[-1:] and i != og_col and self.get_item_from_board(row, i) != "  ":
                        total_hit_enemy_pieces += 1
                if total_hit_enemy_pieces > 1:
                    print("You cannot move through more than one enemy piece!")
                    return False

            # Column check

            if og_col == col:
                total_hit_enemy_pieces = 0
                # Check if the rook is moving through a piece of its own color
                for i in range(min(og_row, row), max(og_row, row)):
                    # Check if the piece is a piece of the same color
                    if self.get_item_from_board(i, col)[-1:] == piece[-1:]:
                        if i != og_row:
                            print("You cannot move through a piece of the same color!")
                            return False                        
                    # Check if the player has gone through an enemy piece
                    if self.get_item_from_board(i, col)[-1:] != piece[-1:] and i != og_row and self.get_item_from_board(i, col) != "  ":
                        total_hit_enemy_pieces += 1
                if total_hit_enemy_pieces > 1:
                    print("You cannot move through more than one enemy piece!")
                    return False

        if piece[:1] == "N":
            # If the knight is moving off the board
            if (row < 0 or row > 7) or (col < 0 or col > 7):
                print("You cannot move a knight off the board!")
                return False

            if (row,col) not in self.knight_move(og_row, og_col):
                print("You cannot move a knight that way!")
                return False

        if piece[:1] == "B":
            total_hit_enemy_pieces = 0
            # Check if the bishop is moving diagonally
            if og_row == row or og_col == col:
                print("You cannot move a bishop parralel with the squares!")
                return False
            for possible_move in self.bishop_move(og_row, og_col, row, col):
                possible_row = possible_move[0]
                possible_col = possible_move[1]
                if possible_row != og_row and possible_col != og_col:
                    # Check if the piece is a piece of the same color
                    if self.get_item_from_board(possible_row, possible_col)[-1:] == piece[-1:]:
                        print("You cannot move through a piece of the same color!")
                        return False                        
                    # Check if the player has gone through an enemy piece
                    if self.get_item_from_board(possible_row, possible_col)[-1:] != piece[-1:] and self.get_item_from_board(possible_row, possible_col) != "  ":
                        total_hit_enemy_pieces += 1
            if total_hit_enemy_pieces > 1:
                print("You cannot move through more than one enemy piece!")
                return False

        if piece[:1] == "Q":
            total_hit_enemy_pieces = 0
            # Check if the bishop is moving diagonally
            for possible_move in self.queen_move(og_row, og_col, row, col):
                possible_row = possible_move[0]
                possible_col = possible_move[1]
                print(possible_row, possible_col)
                if possible_row != og_row and possible_col != og_col:
                    # Check if the piece is a piece of the same color
                    if self.get_item_from_board(possible_row, possible_col)[-1:] == piece[-1:]:
                        print("You cannot move through a piece of the same color!")
                        return False                        
                    # Check if the player has gone through an enemy piece
                if self.get_item_from_board(possible_row, possible_col)[-1:] != piece[-1:] and self.get_item_from_board(possible_row, possible_col) != "  ":
                    total_hit_enemy_pieces += 1
            if total_hit_enemy_pieces > 1:
                print("You cannot move through more than one enemy piece!")
                return False

        if piece[:1] == "K":
            # Check if the king is moving more than 1 space
            if abs(row - og_row) > 1 or abs(col - og_col) > 1:
                print("You cannot move a king more than one space!")
                return False
            # Check if the king is moving into a space that is not empty
            if (row,col) not in self.king_move(og_row, og_col, row, col):
                print("You cannot move a king that way!")
                return False

        return True


    def update_board(self, og_row, og_col, row, col):
        # Update the number of pieces each player has
        if self.get_item_from_board(row, col)[-1:] == "w":
            self.white_pieces.remove(self.get_item_from_board(row, col))
        if self.get_item_from_board(row, col)[-1:] == "b":
            self.black_pieces.remove(self.get_item_from_board(row, col))
        # Update the board with the new move
        self.board[row][col] = self.get_item_from_board(og_row,og_col)
        self.board[og_row][og_col] = "  "
        
        self.alternate_move()