from pickle import FALSE
from checkers_classes import Board
class Helper:
    def __init__(self):
        self.game_in_progress = 0
        self.game_board = Board()
        print(self.game_board.placement['AA'])

    def print_board(self):
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

        print("\nCurrent board:")
        row_index = 0
        for row in self.game_board.board:
            position_index = 0
            for position in row:
                piece_index = 0
                for piece in self.game_board.placement:
                    #print(self.game_board.placement[piece])
                    if self.game_board.placement[piece] == self.game_board.board[row_index][position_index]: #check if for each board position there is a piece there #list index out of range
                        print(piece, end=' ')
                        piece_index = piece_index + 1
                        break
                    elif piece_index >= 23:
                        print("==", end=' ')
                        break         
                    piece_index = piece_index + 1
                position_index = position_index + 1
            row_index = row_index + 1
            print()

    # def move_piece(self):
    #     choice = input("Please select piece to move: ")
    #     if (choice in ['AA', 'BB', 'CC', 'DD', 'EE', 'FF', 'GG', 'HH', 'II', 'JJ', 'KK', 'LL']):
    #         print("You are about to move piece " + choice)
    #         new_position = input("Where do you want to move it?: ")
    #         if (new_position in ['a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8', 'a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7', 'a6', 'b6', 'c6', 'd6', 'e6', 
    #         'f6', 'g6', 'h6', 'a5', 'b5', 'c5', 'd5', 'e5', 'f5', 'g5', 'h5','a4', 'b4', 'c4', 'd4', 'e4', 'f4', 'g4', 'h4','a3', 'b3', 'c3', 'd3', 'e3', 
    #         'f3', 'g3', 'h3', 'a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2', 'a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1']):
                
    #     return 0

    def initialize_game(self):
        return 0


    def show_menu(self):
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
                    self.show_menu()
                elif choice == 's':
                    self.print_board()
                    self.show_menu()
                elif choice == 'm':
                    print('Here method for making moves on the board')
                    self.show_menu()
                else:
                    self.show_menu()
