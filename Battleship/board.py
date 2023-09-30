from battleship import Battleship

class Board:
    '''Board class for Battleship game'''

    def __init__(self, dimensions, ships):
        self._user_board = [] 
        self._dimensions = dimensions
        self._ship_locations = {}
        self._ships_left = ships
        self._moves = set()

        for i in range(dimensions):
            self._user_board.append(["O"] * dimensions)

    def place_ship(self, x_coord, y_coord, orientation, length):
        ''' places ship on board, true if successful, false if not'''
        
        new_ship = Battleship(length)
        cells_placed = set()

        if orientation == "horizontal":
            if x_coord + length > self._dimensions:
                return False
            for i in range(length):
                x,y = x_coord + i, y_coord
                if (x,y) in self._ship_locations:
                    return False
            for i in range(length):
                x,y = x_coord + i, y_coord
                self._ship_locations[(x,y)] = new_ship 
                cells_placed.add((x,y))

        elif orientation == "vertical":
            if y_coord + length > self._dimensions:
                return False
            for i in range(length):
                x,y = x_coord, y_coord + i
                if (x,y) in self._ship_locations:
                    return False
            for i in range(length):
                x,y = x_coord, y_coord + i
                self._ship_locations[(x,y)] = new_ship 
                cells_placed.add((x,y))
        
        new_ship.set_ship(cells_placed)
            
        return True
    
    def attack(self, x_coord, y_coord):
        '''player attacks board, returns true if hit, false if miss'''
        if x_coord < 0 or x_coord >= self._dimensions or y_coord < 0 or y_coord >= self._dimensions:
            return "Invalid coordinates"
        
        if (x_coord,y_coord) in self._moves:
            return "Already attacked!"
        elif (x_coord,y_coord) in self._ship_locations:
            ship = self._ship_locations[(x_coord,y_coord)]
            ship.hit(x_coord,y_coord)
            self._moves.add((x_coord,y_coord))
            self._user_board[x_coord][y_coord] = "S"
            if ship.is_sunk():
                self._ships_left -= 1
                return "Ship sunk! Ships left: " + str(self._ships_left)
            return "Ship hit!"
        else:
            self._moves.add((x_coord,y_coord))
            self._user_board[x_coord][y_coord] = "X"
            return "Ship missed!"
    
    def is_game_over(self):
        '''returns true if all ships have been sunk'''

        return self._ships_left == 0

    def print_board(self):
        ''' prints board out for user '''

        res = "  " + " ".join([str(i) for i in range(self._dimensions)])
        print(res)
        for i,row in enumerate(self._user_board):
            res = str(i) + " " + (" ".join(row))
            print(res)


