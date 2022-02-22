import pygame
from game import tictactoe
from computer import cpu
from player import human

# Creates the game and sets the players
def main():
	game = tictactoe()
	run(game, player1 = 'human', player2 = 'cpu')   					# Create the game class and set the players

# Runs through the game
# Inputs: game - the tic-tac-toe class
#		  player1 (default = 'human') - string denoting type of player 1
#		  player2 (default = 'cpu') - string denoting type of player 2
def run(game, player1 = 'human', player2 = 'cpu'):
	players = []														# Convert the input strings to their corresponding 
	if (player1 == 'human'):											# player classes
		players.append(human(player = 1))
	else:
		players.append(cpu(player = 1))
	if (player2 == 'human'):
		players.append(human(player = 2))
	else:
		players.append(cpu(player = 2))

	running = True
	turn = 0
	done = False
	while running:
		for event in pygame.event.get():								# List of events: https://www.pygame.org/docs/ref/event.html
			if event.type == pygame.QUIT:								# The GUI was closed
				running = False
			if event.type == pygame.MOUSEBUTTONUP:
				if (done):
					game = tictactoe()									# If a game just finished, reset it and continue
					done = False
					turn = 0
				else:
					i = players[turn].move(game.board)					# Get player input
					turn = game.move(i) - 1
					winner = game.checkwin()
					if (winner != -1):
						done = True
		if (players[turn].type == 'cpu' and done == False):				# The cpu input checker runs continously
			i = players[turn].move(game.board)							# calling convention for cpu input is identical to human player
			turn = game.move(i) - 1
			winner = game.checkwin()
			if (winner != -1):
				done = True
						
    
if __name__=="__main__":
    main()