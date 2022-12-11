#TODO
#player beating enemy pieces movement (recursion to check after one beating?)
#win condition check (0 pieces left)
#enemy movement
#changing to queen piece after reaching last line and movement for it 
#changing to queen piece for enemy too after reaching first line

from pickle import FALSE
from checkers_classes import Board
class Helper:
    def __init__(self):
        self.game_in_progress = 0
        self.game_board = Board()

    def print_board(self):
        print("\nCurrent board:")
        row_index = 0
        row_print = 8
        print ('   A   B   C   D   E   F   G   H')
        print ('  -------------------------------')
        for row in self.game_board.board:
            position_index = 0
            print('' + str(row_print) + '|', end=' ')
            for position in row:
                piece_index = 0
                for piece in self.game_board.placement:
                    #print(self.game_board.placement[piece])
                    if self.game_board.placement[piece] == self.game_board.board[row_index][position_index]: #check if for each board position there is a piece there #list index out of range
                        print(piece +' ', end=' ')
                        piece_index = piece_index + 1
                        break
                    elif piece_index >= 23:
                        print("-- ", end=' ')
                        break         
                    piece_index = piece_index + 1
                position_index = position_index + 1
            row_index = row_index + 1
            print('|' + str(row_print), end=' ')
            row_print = row_print -1
            print()
        print ('  -------------------------------')
        print ('   A   B   C   D   E   F   G   H')


    def move_piece_player(self): #works! For moving pieces alone, but works!
        choice = input("Please select piece to move: ")
        if (choice in ['AA', 'BB', 'CC', 'DD', 'EE', 'FF', 'GG', 'HH', 'II', 'JJ', 'KK', 'LL']):
            print("You are about to move piece " + choice)
            new_position = input("Where do you want to move it?: ")
            # if (new_position in ['a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8', 'a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7', 'a6', 'b6', 'c6', 'd6', 'e6', 
            # 'f6', 'g6', 'h6', 'a5', 'b5', 'c5', 'd5', 'e5', 'f5', 'g5', 'h5','a4', 'b4', 'c4', 'd4', 'e4', 'f4', 'g4', 'h4','a3', 'b3', 'c3', 'd3', 'e3', 
            # 'f3', 'g3', 'h3', 'a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2', 'a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1']):
                
            if (new_position in self.possible_moves_player(choice)): #checks if piece can move there and if there arent any other pieces on that field.
                # print(self.game_board.placement[choice][0]) #take first value from board numbering (a,b,c,d,e,f,g,h)
                # print(self.game_board.placement[choice][1]) #take second value from board numbering (1,2,3,4,5,6,7,8)
                
                for key in self.game_board.placement:
                    if (self.game_board.placement[key] == new_position):
                        print("Wrong destination, another piece is already on that position")
                        return 0
                self.game_board.placement[choice] = new_position
            
            else:
                print('You cannot move there')
                self.show_menu()


                #check possible moves. board[0][0] can only move to board [1][1]. 
                #Board [0][1] can move to board [1][0] and board [1][2]
                #Board [0][2] can move to board[1][1] and board [1][3]
                #Possible moves: board[<1 or >6] only one move. Board[x][0] only to board [x+1][0]
                #board[x][7] only to board[x+1][6]
                #else can move to board[x+1][y-1] or board[x+1][y+1]
        return 0

    def move_piece_enemy(self): 
        #if can beat player piece, beat it. Otherwise, random move. Later can improve it
        return 0

    def check_pieces_left(self):
        black_pieces_count = 0
        white_pieces_count = 0
        for key in self.game_board.placement:
            if (key in ['AA', 'BB', 'CC', 'DD', 'EE', 'FF', 'GG', 'HH', 'II', 'JJ', 'KK', 'LL']):
                black_pieces_count = black_pieces_count + 1
            else:
                white_pieces_count = white_pieces_count + 1
        print('White pieces left: ' + str(white_pieces_count))
        print('Black pieces left: ' + str(black_pieces_count))
        if black_pieces_count == 0:
            print("You have won!")
            self.game_in_progress = 0
        if white_pieces_count == 0:
            print("Computer has won")
            self.game_in_progress = 0
        return 0


    def possible_moves_player(self, choice):
        # print(self.game_board.placement[choice][0]) #take first value from board numbering (a,b,c,d,e,f,g,h)
        # print(self.game_board.placement[choice][1]) #take second value from board numbering (1,2,3,4,5,6,7,8)
        board_letter = self.game_board.placement[choice][0]
        board_number = self.game_board.placement[choice][1]

        moves = []

        if board_letter == 'a': #if piece is in the first column
            temp_numb = int(board_number) + 1
            temp_letter = chr(ord(board_letter) + 1)
            print(temp_letter)
            combined = temp_letter + str(temp_numb)
            print(combined)
            moves.append(combined) 
            print(moves)
        elif board_letter == 'h': #if piece is in the last column
            temp_numb = int(board_number) - 1
            temp_letter = chr(ord(board_letter) - 1)
            combined = temp_letter + str(temp_numb)
            moves.append(combined) 
        else:
            temp_numb = int(board_number) + 1
            temp_letter = chr(ord(board_letter) + 1)
            combined = temp_letter + str(temp_numb)
            moves.append(combined)
            temp_numb = int(board_number) - 1
            temp_letter = chr(ord(board_letter) + 1)
            combined = temp_letter + str(temp_numb)
            moves.append(combined) 
        return moves
    
    def initialize_game(self):
        return 0

    def show_menu(self):
        self.check_pieces_left()
        print()
        if (self.game_in_progress == 0):
            print("Welcome to Checkers!")
            print("Play new game - n")
            print("Quit - q")
            choice = input("Your choice: ")
            if (choice in ['n', 'q']):
                if choice == "q":
                    print("Thanks for playing!")
                    quit()
                elif choice == "n":
                    #new game
                    self.game_in_progress = 1
                    self.game_board.initialize_game()
                    self.show_menu()
                else:
                    self.show_menu()
        elif (self.game_in_progress == 1):
            print("Show board - s")
            print("Make a move - m")
            print("New game - n")
            print("Quit - q")
            choice = input("Your choice: ")
            if (choice in ['s', 'm', 'n', 'q']):
                if choice == "q":
                    print("Thanks for playing!")
                    quit()
                elif choice == "n":
                    #new game
                    print('Here I want to reinitialize the board and clean it from any movement')
                    self.game_board.initialize_game()
                    self.show_menu()
                elif choice == 's':
                    self.print_board()
                    self.show_menu()
                elif choice == 'm':
                    self.move_piece_player()
                    self.show_menu()
                else:
                    self.show_menu()

    # def move_piece(self): #works! For moving pieces alone, but works!
    #     choice = input("Please select piece to move: ")
    #     if (choice in ['AA', 'BB', 'CC', 'DD', 'EE', 'FF', 'GG', 'HH', 'II', 'JJ', 'KK', 'LL']):
    #         print("You are about to move piece " + choice)
    #         new_position = input("Where do you want to move it?: ")
    #         if (new_position in ['a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8', 'a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7', 'a6', 'b6', 'c6', 'd6', 'e6', 
    #         'f6', 'g6', 'h6', 'a5', 'b5', 'c5', 'd5', 'e5', 'f5', 'g5', 'h5','a4', 'b4', 'c4', 'd4', 'e4', 'f4', 'g4', 'h4','a3', 'b3', 'c3', 'd3', 'e3', 
    #         'f3', 'g3', 'h3', 'a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2', 'a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1']):
    #             self.game_board.placement[choice] = new_position
    #     return 0


    #    def print_board(self):
        #print board with placement of pieces
        # for row in board:
        #     position_index = 0
        #     for position in row:
        #         print(position, end=' ')
        #     print()
        #     print()

        # print("\nCurrent board:")
        # row_index = 0
        # for row in self.game_board.board:
        #     position_index = 0
        #     for position in row:
        #         piece_index = 0
        #         for piece in self.game_board.placement:
        #             if self.game_board.placement[piece_index][1] == self.game_board.board[row_index][position_index]: #check if for each board position there is a piece there #list index out of range
        #                 print(self.game_board.placement[piece_index][0], end=' ')
        #                 piece_index = piece_index + 1
        #                 break
        #             elif piece_index >= 23:
        #                 print("==", end=' ')
        #                 break         
        #             piece_index = piece_index + 1
        #         position_index = position_index + 1
        #     row_index = row_index + 1
        #     print()