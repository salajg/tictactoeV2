import pygame
from game import *

class human:

    # Initializes a human player
    # Inputs: player (default = 1) - determines if player is going first or second
    def __init__(self, player = 1):
        self.player = player
        self.type = 'human'

    # Find a move to make
    # Inputs: board - the current game board
    # Outputs: An index on the game board or -1 if 
    #          the click position is invalid
    def move(self, board):
        if (0 not in board):
            return -1
        pos = pygame.mouse.get_pos()                                            # Get posistion of most recent mouse click
        i = self.poscalc(pos)                                                   # Convert that mouse click to a index on the board
        
        if (board[i] != 0 or i == -1):                                          # If position is taken return an error 
            return -1
        return i

    # Convert the mouse position to a index on the board
    # Inputs: pos - a tuple indicating position of mouse click
    # Outputs: An index on the game board  or -1 if 
    #          the click position is invalid
    def poscalc(self, pos):
        if (pos[0] < 100 or pos[0] > 400 or pos[1] < 100 or pos[1] > 400):      # Check if the click was out of bounds of the grid
            return -1
        x = int((pos[0] - 100)/100)
        y = int((pos[1] - 100)/100)
        return y*3+x
