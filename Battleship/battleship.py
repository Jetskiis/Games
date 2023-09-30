class Battleship:
    '''Ship class for battleship object'''
    
    def __init__(self, length):
        self._lives_left = length
        self._cells_placed = set()
    
    def set_ship(self,coords):
        '''sets the coordinates where ship resides  '''
        self._cells_placed = coords
    
    def hit(self, x_coord, y_coord):
        '''decrements lives left when hit'''
        if (x_coord,y_coord) in self._cells_placed:
            self._lives_left -= 1
    
    def is_sunk(self):
        '''returns True if ship is sunk'''
        if self._lives_left == 0:
            return True
        else:
            return False
        
        
        
    
    
    