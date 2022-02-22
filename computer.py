import random
import numpy as np
from game import *

class cpu:

    # Initializes a computer opponent
    # Inputs: player (default = 2) - determines if cpu is going first or second
    #         dumb (default = False) - a dumb cpu will choose moves randomly
    def __init__(self, player = 2, dumb = False):
        self.player = player
        self.type = "cpu"
        self.dumb = dumb

    # Find a move to make
    # Inputs: board - the current game board
    # Outputs: An index on the game board or -1 if 
    #          the board is full
    # This algorithm follows a basic win or block strategy
    def move(self, board):
        if (self.dumb):
            return self.moverandom(board)
        arr = np.arange(9)
        np.random.shuffle(np.arange(9))                                                 # A shuffled array is used to 
        for i in arr:                                                                   # emulate randomness in its moves
            if (board[i] == 0):
                game2 = tictactoe(graphics = False)                                     # A duplicate game is created to simulate potential moves
                game2.board = board.copy()
                game2.player = self.player
                _ = game2.move(i)
                winner = game2.checkwin()
                if (winner == self.player):
                    return i                                                            # If a possible win is detected take it immediatly
                for j in arr:
                    game2.board = board.copy()                                          # Scan the board for potential ways for the opponent to win
                    game2.player = self.player
                    _ = game2.move(i)
                    if (board[j] == 0):
                        _ = game2.move(j)
                        winner = game2.checkwin()
                        if (winner != self.player and winner != -1 and winner != 0):
                            return j                                                    # If the opponent can win try and block that position
        return self.moverandom(board)                                                   # If nothing interesting found, return a random move

    # Finds a random move to make
    # Inputs: board - the current game board
    # Outputs: An index on the game board or -1 if 
    #          the board is full
    def moverandom(self, board):
        i = random.randint(0, 8)
        if (0 not in board):
            return -1
        while (board[i] != 0):
            i = random.randint(0, 8)                                                    # Keep choosing random number until a valid move is found
        return i