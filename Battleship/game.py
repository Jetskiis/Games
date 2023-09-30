from board import Board
import pyinputplus
import random

class Game:
    '''Handles all game logic'''
    def __init__(self):
        self.board = None
        self.num_ships = 0
        self.start_game() 

    def start_game(self):
        '''initializes the game'''
        moves = 0
        
        dimensions = self.check_input("Type in a number for the size of the board (e.g. 10 for a 10x10 board) ", None)

        print("Initializing game with a " + str(dimensions) + "x" + str(dimensions) + " board with the following ships randomly placed: Carrier (5 spaces), Battleship (4 spaces), Cruiser (3 spaces), Submarine (3 spaces), Destroyer (2 space)")
        print()
        self.board = Board(dimensions, 5)
        self.board.print_board()
        
        #place ships
        while self.num_ships < 5:
            rand_x, rand_y = random.randint(0,dimensions-1), random.randint(0,dimensions-1)
            orientation = random.choice(["horizontal","vertical"])
            
            if self.num_ships == 0:
                if self.board.place_ship(rand_x,rand_y,orientation,5):
                    self.num_ships += 1
                
            elif self.num_ships == 1:
                if self.board.place_ship(rand_x,rand_y,orientation,4):
                    self.num_ships += 1
            
            elif self.num_ships == 2:
                if self.board.place_ship(rand_x,rand_y,orientation,3):
                    self.num_ships += 1
            
            elif self.num_ships == 3:
                if self.board.place_ship(rand_x,rand_y,orientation,3):
                    self.num_ships += 1
            
            elif self.num_ships == 4:
                if self.board.place_ship(rand_x,rand_y,orientation,2):
                    self.num_ships += 1
                
        #game loop
        while self.board.is_game_over() == False:
            x = self.check_input("Enter x coordinate to attack:", dimensions)
            y = self.check_input("Enter y coordinate to attack:", dimensions) 
            print()
            status = self.board.attack(y,x) #actually gets swapped
            if status != "Invalid Coordinates":
                moves += 1
            print(status)
            print()
            self.board.print_board()
            print()
        
        print("You won in " + str(moves) + " moves!")
    
    def check_input(self,user_message, dimensions):
        '''asks user for input and validates user input'''
        while True:
            try:
                user_input = int(input(user_message))
                if dimensions != None:
                    if user_input >= dimensions or user_input < 0:
                        print("Please enter a valid number")
                        continue
                return user_input
            except ValueError:
                print("Please enter a valid number")
                continue
        