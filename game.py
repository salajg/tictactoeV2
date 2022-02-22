import pygame

class tictactoe:

	# Initialize an empty game board and set the starting player
	# Inputs: graphics (default = True) - toggle to create GUI
	def __init__(self, graphics = True):
		self.board = [0, 0, 0, 0, 0, 0, 0, 0, 0]								# Create an empty game board
		self.player = 1
		self.graphics = graphics
		if (graphics):
			self.drawgraphics()
	
	# Initiazlizes the pygame graphics API and draws game board
	def drawgraphics(self):
		pygame.init()
		logo = pygame.image.load("graphics/logo32x32.png")
		pygame.display.set_icon(logo)
		pygame.display.set_caption("Tic-Tac-Toe")
		self.screen = pygame.display.set_mode((500,500))						# Default screen resolution 500x500 
																				# CHANGING THIS WILL CAUSE OTHER LOGIC TO FAIL
		background = pygame.image.load("graphics/background.png")
		self.screen.blit(background, (0,0))

		pygame.draw.line(self.screen, (150,150,150), (200, 100), (200, 400))	# These 4 line are responsible to drawing the grid
		pygame.draw.line(self.screen, (150,150,150), (300, 100), (300, 400))
		pygame.draw.line(self.screen, (150,150,150), (100, 200), (400, 200))
		pygame.draw.line(self.screen, (150,150,150), (100, 300), (400, 300))

		pygame.font.init()
		myfont = pygame.font.SysFont('Comic Sans MS', 50)						# Comic Sans because why not?
		header = myfont.render('Tic-Tac-Toe', False, (255, 255, 255))
		self.screen.blit(header,(100,25))

		pygame.display.flip()													# This pushes our changes to the GUI

	# Called after a player makes a move
	# Updates the GUI to the current state of board
	def update(self):
		for i in range(len(self.board)):										# Iterate through the entire game board
			x = 150 + (100 * (i % 3))											# x and y are the corners of each square in the grid
			y = 150 + (100 * int((i / 3)))
			if (self.board[i] == 2):
				pygame.draw.circle(self.screen, (255,255,255), (x, y), 30, width = 1)    	# Draw circle for player O
			elif (self.board[i] == 1):
				pygame.draw.line(self.screen, (255,255,255), (x+30, y+30), (x-30, y-30))	# Draw 2 lines for player X
				pygame.draw.line(self.screen, (255,255,255), (x-30, y+30), (x+30, y-30))
		pygame.display.flip()
	
	# Makes a move to the game
	# Inputs: idx - the spot the player wants to make their move to
	# Outputs: the next player or -1 if move is invalid
	def move(self, idx):
		if (self.board[idx] == 0 and idx >= 0 and idx <=8):						# Check if the potential move is valid
			self.board[idx] = self.player
			self.player = self.player%2+1										# Changes from player 1 -> 2 and vice versa
			if (self.graphics):
				self.update()
			return self.player
		else:
			return -1

	# Scans the game board for a valid winning orientation
	# Also uses pygame to print winning line and text
	# Outputs: -1 if no winner
	#		    0 if tie
	#			1 if player 1 won
	#      		2 if player 2 won
	def checkwin(self):
		winner = -1
		start = (0 , 0)  														# start and end are used to draw the winning line
		end = (0 , 0)
		for i in range(3):
			if (self.board[i*3]!= 0 and self.board[i*3] == self.board[i*3+1] and self.board[i*3+1] == self.board[i*3+2]):
				start = (100, 150 + i*100)										# Horozontal win
				end = (400, 150 + i*100)
				winner = self.board[i*3]
			if (self.board[i]!= 0 and self.board[i] == self.board[i+3] and self.board[i+3] == self.board[i+6]):
				start = (150 + i*100, 100)										# Vertical Win
				end = (150 + i*100, 400)
				winner = self.board[i]
		if (self.board[0]!= 0 and self.board[0] == self.board[4] and self.board[4] == self.board[8]):
			start = (100, 100)													# Negative slope win
			end = (400, 400)
			winner = self.board[0]
		if (self.board[2]!= 0 and self.board[2] == self.board[4] and self.board[4] == self.board[6]):
			start = (400, 100)													# Positive slope ein
			end = (100, 400)
			winner = self.board[2]
		message = ""															# The message is used to print on GUI
		if (0 not in self.board and winner == -1):
			message = "Tie"
			winner = 0
		if (winner == 1):
			message = "Player X Wins"
		elif (winner == 2):
			message = "Player O Wins"
		if (self.graphics and winner != -1):
			pygame.font.init()
			myfont = pygame.font.SysFont('Comic Sans MS', 20)					# Print the message at the bottom of the screen
			pygame.draw.line(self.screen, (255,0,0), start, end)
			result = myfont.render(message, False, (255, 255, 255))
			self.screen.blit(result,(100,425))
			pygame.display.flip()
		return winner

