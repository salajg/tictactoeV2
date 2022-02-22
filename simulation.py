from game import *
from computer import cpu
import tqdm
import matplotlib.pyplot as plt

# epochs - number of games to simulate
epochs = 1000

# Runs the game a defined amount of iterations and plots the results
def main():
	results = [0,0,0]
	players = [cpu(player = 1, dumb = False), cpu(player = 2, dumb = True)]				# Changes type of cpu to simulate with
	for i in tqdm.tqdm(range(epochs)):
		game = tictactoe(graphics = False)												# Reset the game after every run and disable GUI
		winner = run(game, players)
		results[winner] += 1
	print("Player 1 winrate: ", results[1]/epochs)										# Print player 1 winrate to terminal
	tags = ['Tie', 'Smart CPU won', 'Dumb CPU won']
	fig = plt.figure()
	plt.bar(tags, results)																# Use a bar graph to represent the entire results
	plt.xlabel("Results of Match")
	plt.ylabel("No. of Occurences")
	plt.title("Tic-Tac-Toe with a Smart CPU vs Dumb CPU")
	plt.show()

# Runs one iteration of the game
# Inputs: players - a list of length 2 containing the classes for player 1 and 2
# Outputs: the result of the match
def run(game, players):
	winner = -1
	turn = 0
	done = False
	while not done:
		if (players[turn].type == 'human'):												# Return error if trying to simulate with humans
			return -1
		if (players[turn].type == 'cpu' and done == False):
			i = players[turn].move(game.board)											# Run an infinite loop until the game has finished
			turn = game.move(i) - 1
			winner = game.checkwin()
			if (winner != -1):
				done = True
	return winner
	
			 
if __name__=="__main__":
	main()