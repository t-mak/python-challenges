#TODO
#DONE - can't beat if no landing possible anymore. Player beating enemy pieces movement - this still needs to check if there are no blocking pieces that don't allow the beating!
#enemy movement
#changing to queen piece after reaching last line and movement for it 
#changing to queen piece for enemy too after reaching first line
#add checking before enemy moves, if there are any left pieces for it

#11.12 22:41 - enemy movement, beating not implemented. Queens not implemented.

import random
from pickle import FALSE
from checkers_classes import Board
import player, computer
# from player import Player

class Helper:
    def __init__(self):
        # self.player = Player()
        self.game_in_progress = 0
        self.game_board = Board()
        self.pieces_number = 24

    def return_key(self, val):
        for key, value in self.game_board.placement.items():
            if value==val:
                return key
        return('Key Not Found')


## GAME METHODS

    ## PRINT BOARD
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
                    elif piece_index >= self.pieces_number - 1:
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

    ## CHECK IF GAME IS STILL IN PROGRESS
    def check_pieces_left(self):
        black_pieces_count = 0
        white_pieces_count = 0
        for key in self.game_board.placement:
            if (key in ['AA', 'BB', 'CC', 'DD', 'EE', 'FF', 'GG', 'HH', 'II', 'JJ', 'KK', 'LL']):
                white_pieces_count = white_pieces_count + 1
            else:
                black_pieces_count = black_pieces_count + 1
        print('White pieces left: ' + str(white_pieces_count))
        print('Black pieces left: ' + str(black_pieces_count))
        if black_pieces_count == 0:
            print("You have won!")
            self.game_in_progress = 0
        if white_pieces_count == 0:
            print("Computer has won")
            self.game_in_progress = 0
        return 0 
    
    # def initialize_game(self):
    #     return 0

    ## SHOW MENU 
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
                    self.player_piece_choice()
                    self.computer_piece_choice()
                    self.show_menu()
                else:
                    self.show_menu()

##PLAYER METHODS
    def player_beat_enemy(self, piece_choice, beating_choice):
        board_letter_player = self.game_board.placement[piece_choice][0]
        board_number_player = self.game_board.placement[piece_choice][1]    
        board_letter_computer = self.game_board.placement[beating_choice][0]
        board_number_computer = self.game_board.placement[beating_choice][1]   

        # print("board letter player: " + board_letter_player) 
        # print("board number player: " + board_number_player)         
        # print("board letter enemy: " + board_letter_computer)   
        # print("board number enemy: " + board_number_computer)

        player_piece = self.return_key(self.game_board.placement[piece_choice])
        enemy_piece = self.return_key(self.game_board.placement[beating_choice])
        # print("Player piece used for beating: " + player_piece)
        # print("Enemy piece used for beating: " + enemy_piece)

        #check positions of player vs enemy piece. Only need to check horizontal positions, as beating is always forward for player
        if (ord(board_letter_player) < ord(board_letter_computer)):
            self.game_board.placement[player_piece] = chr(ord(board_letter_computer) + 1) + str(int(board_number_computer) + 1)
            print(chr(ord(board_letter_computer) + 1) + str(int(board_number_computer) + 1))
        else:
            self.game_board.placement[player_piece] = chr(ord(board_letter_computer) - 1) + str(int(board_number_computer) + 1)
        self.pieces_number = self.pieces_number - 1
        self.game_board.placement.pop(enemy_piece)
        return 

    def player_piece_choice(self):
            piece_choice = input("Please select piece to move: ")
            if (piece_choice in ['AA', 'BB', 'CC', 'DD', 'EE', 'FF', 'GG', 'HH', 'II', 'JJ', 'KK', 'LL']):
                print("You are about to move piece " + piece_choice)
                # beating = []
                # beating = self.possible_beatings_player(piece_choice)
                self.move_piece_player(piece_choice, beaten_enemy_already = 0)

    def player_beating_enemy(self, piece_choice, possible_beatings):
        beating_choice = input("Which piece do you want to beat?: ")
        self.player_beat_enemy(piece_choice, beating_choice)
        possible_beatings.remove(beating_choice)
        # self.enemy_beating(piece_choice, beating)
        return 
        

    def move_piece_player(self, piece_choice, beaten_enemy_already): #works! For moving pieces alone, but works!
        #variable to check if I already beaten someone with this piece. If so, I can only beat again, cannot move
        possible_beatings = []
        possible_beatings = self.possible_beatings_player(piece_choice)
        if (len(possible_beatings) >0):
            print("You must beat the enemy piece")
            print("Possible beatings: ")
            for n in possible_beatings:
                print(n)
            self.player_beating_enemy(piece_choice, possible_beatings)
            beaten_enemy_already = 1
            self.move_piece_player(piece_choice, beaten_enemy_already)
        if beaten_enemy_already != 1:
            new_position = input("Where do you want to move it?: ")
            if (new_position in self.possible_moves_player(piece_choice)): #checks if piece can move there and if there arent any other pieces on that field.
                for key in self.game_board.placement:
                    if (self.game_board.placement[key] == new_position):
                        print("Wrong destination, another piece is already on that position")
                        return 0
                self.game_board.placement[piece_choice] = new_position
            else:
                print('You cannot move there')
                self.show_menu() 
        #self.enemy_piece_choice() #enemy turn     #HERE ERROR    
        return 0


    def possible_beatings_player(self, choice): #11.12TODO - this still needs to check if there are no blocking pieces that don't allow the beating!
        player_possible_moves = self.possible_moves_player(choice) #this returns fields with possible moves, NOT enemy pieces (e.g a2, c2 not 01, 02). Need to find the key of the value
        
        #enemy_field_check is now a list of possible moves of the player. Now I need to check if there are any enemy pieces in those fields
        #check if in a field where player can move, there is an enemy piece
        beating = []
        for key in self.game_board.placement:
            if key in ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']:
                if (self.game_board.placement[key] in player_possible_moves): # self.game_board.placement[key] is like self.game_board.placement['01'] which returns value (field like a1) 
                    if int(self.game_board.placement[key][1]) < 8: #check if there is space to move, if computer piece is not at row 8 

##                      checking here if I can land after beating enemy piece

                        #choice #this is player piece
                        #key #this is enemy piece
                        board_letter_player = self.game_board.placement[choice][0]
                        board_letter_computer = self.game_board.placement[key][0]
                        board_number_computer = self.game_board.placement[key][1] 

                        check_if_taken = 0  

                        #check positions of player vs enemy piece. Only need to check horizontal positions, as beating is always forward for player
                        #player at e1 wants to be enemy at d2 -> I need to check if c3 is free for landing
                        if (ord(board_letter_player) < ord(board_letter_computer)): #if enemy piece is further to the right on board
                            temp_value = chr(ord(board_letter_computer) + 1) + str(int(board_number_computer) + 1) #temp_value holds field for landing I would need free to beat
                            print(self.return_key(temp_value)) 
                            check_if_taken = self.return_key(temp_value)
                        #I need to get cordinates behind computer piece and then check if there is another piece there from the placement list
                        else:
                            temp_value = chr(ord(board_letter_computer) - 1) + str(int(board_number_computer) + 1)
                            print(self.return_key(temp_value)) 
                            check_if_taken = self.return_key(temp_value)
                        # if return_key(): #now I need to check if no pieces are behind computer piece. 
                        if check_if_taken in self.game_board.placement:
                            print("Can't land after beating, beating impossible")
                        else:
                            print("Possible beating of enemy piece in field: " + self.game_board.placement[key])
                            beating.append(key)
        return beating


    def possible_moves_player(self, choice):
        print("Inside possible moves player")
        # print(choice)
        # print(self.game_board.placement[choice][0]) #take first value from board numbering (a,b,c,d,e,f,g,h)
        # print(self.game_board.placement[choice][1]) #take second value from board numbering (1,2,3,4,5,6,7,8)
        board_letter = self.game_board.placement[choice][0]
        board_number = self.game_board.placement[choice][1]
        moves = []

        if board_letter == 'a': #if piece is in the first column
            temp_numb = int(board_number) + 1
            temp_letter = chr(ord(board_letter) + 1)
            combined = temp_letter + str(temp_numb)
            moves.append(combined) 
        elif board_letter == 'h': #if piece is in the last column
            temp_numb = int(board_number) + 1
            temp_letter = chr(ord(board_letter) - 1)
            combined = temp_letter + str(temp_numb)
            moves.append(combined) 
        else:
            temp_numb = int(board_number) + 1
            temp_letter = chr(ord(board_letter) + 1)
            combined = temp_letter + str(temp_numb)
            moves.append(combined)
            temp_numb = int(board_number) + 1
            temp_letter = chr(ord(board_letter) - 1)
            combined = temp_letter + str(temp_numb)
            moves.append(combined) 
        return moves


##COMPUTER METHODS

    def computer_piece_choice(self):
        print("Computer is choosing a piece...")
        self.computer_possible_beatings('10')
        #check if any piece can beat player piece, if so then use it
        #if can't beat any player piece, move forward with a piece that has movement possible

    ##Works correctly. For 10 gave e5, c5 as possible moves.
    def computer_possible_moves(self, choice):
        print("Inside possible moves computer")
        # print(choice)
        # print(self.game_board.placement[choice][0]) #take first value from board numbering (a,b,c,d,e,f,g,h)
        # print(self.game_board.placement[choice][1]) #take second value from board numbering (1,2,3,4,5,6,7,8)
        board_letter = self.game_board.placement[choice][0]
        board_number = self.game_board.placement[choice][1]
        moves = []

        if board_letter == 'a': #if piece is in the first column
            temp_numb = int(board_number) - 1
            temp_letter = chr(ord(board_letter) + 1)
            combined = temp_letter + str(temp_numb)
            moves.append(combined) 
        elif board_letter == 'h': #if piece is in the last column
            temp_numb = int(board_number) - 1
            temp_letter = chr(ord(board_letter) - 1)
            combined = temp_letter + str(temp_numb)
            moves.append(combined) 
        else:
            temp_numb = int(board_number) - 1
            temp_letter = chr(ord(board_letter) + 1)
            combined = temp_letter + str(temp_numb)
            moves.append(combined)
            temp_numb = int(board_number) - 1
            temp_letter = chr(ord(board_letter) - 1)
            combined = temp_letter + str(temp_numb)
            moves.append(combined) 
        return moves

    ##Works correctly. Correctly checks for possible beatings of player and if landing is possible
    def computer_possible_beatings(self, choice): #11.12TODO - this still needs to check if there are no blocking pieces that don't allow the beating!
            computer_possible_moves = self.computer_possible_moves(choice) #this returns fields with possible moves, NOT enemy pieces (e.g a2, c2 not 01, 02). Need to find the key of the value
            
            for move in computer_possible_moves:
                print("Computer piece" + choice + "can move to field: " + move)
            
            beating = []
            for key in self.game_board.placement:
                if key in ['AA', 'BB', 'CC', 'DD', 'EE', 'FF', 'GG', 'HH', 'II', 'JJ', 'KK', 'LL']:
                    if (self.game_board.placement[key] in computer_possible_moves): # self.game_board.placement[key] is like self.game_board.placement['01'] which returns value (field like a1) 
                        if int(self.game_board.placement[key][1]) > 1: #check if there is space to move, if computer piece is not at row 1 

    ##                      checking here if I can land after beating enemy piece

                            #choice #this is player piece
                            #key #this is enemy piece

                            board_letter_computer = self.game_board.placement[choice][0]
                            board_number_computer = self.game_board.placement[choice][1] 
                            board_letter_player = self.game_board.placement[key][0]
                            board_number_player = self.game_board.placement[key][1]
                            
                            check_if_taken = 0  

                            #check positions of player vs enemy piece. Only need to check horizontal positions, as beating is always forward for player
                            #player at e1 wants to be enemy at d2 -> I need to check if c3 is free for landing
                            if (ord(board_letter_computer) < ord(board_letter_player)): #if player piece is further to the right on board
                                temp_value = chr(ord(board_letter_player) + 1) + str(int(board_number_player) - 1) #temp_value holds field for landing I would need free to beat
                                # print(self.return_key(temp_value)) 
                                check_if_taken = self.return_key(temp_value)
                            #I need to get cordinates behind computer piece and then check if there is another piece there from the placement list
                            else:
                                temp_value = chr(ord(board_letter_player) - 1) + str(int(board_number_player) - 1)
                                # print(self.return_key(temp_value)) 
                                check_if_taken = self.return_key(temp_value)
                            # if return_key(): #now I need to check if no pieces are behind computer piece. 
                            if check_if_taken in self.game_board.placement:
                                print("Can't land after beating, beating impossible")
                            else:
                                print("Possible beating of enemy piece in field: " + self.game_board.placement[key])
                                beating.append(key)
            return beating