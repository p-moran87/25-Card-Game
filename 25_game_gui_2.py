"""
File: 25_game_gui.py
Author: Paul Moran

GUI based version of the 25 card game
"""

from tkinter import *
from TwentyFive_2 import CardGame

class TwentyFiveGUI(Frame):

	def __init__(self):
		Frame.__init__(self, bg='darkgreen')
		self.master.title("TwentyFive")
		self.master.configure(bg='darkgreen')
		self.master.geometry("800x600")
		self.grid()
		
		self._newGameButton = Button(self, text = "New Game", command = self._newGame)
		self._newGameButton.grid(row = 0, column = 7)

		self._dealAgainButton = Button(self, text = "Deal Again", command = self._dealAgain) #self._dealAgain)
		self._dealAgainButton.grid(row = 1, column = 7)

		self._computerVar = Label(self, text="Computer")
		self._computerVar.grid(row = 2, column = 0, columnspan = 5)

		self._computerScore = StringVar()
		self._computerScoreField = Entry(self, width = 3, textvariable = self._computerScore)
		self._computerScoreField.grid(row = 2, column = 3, columnspan = 1)

		# Add the panes for the player and dealer cards
		self._computerPane = Frame(self)
		self._computerPane.grid(row = 3, column = 0, columnspan = 5)

		self._trumpsPane = Frame(self)
		self._trumpsPane.grid(row = 7, column = 0, columnspan = 5)

		# Add the status field for robbing
		self._statusVar1 = StringVar()
		self._statusField1 = Entry(self, width = 25, textvariable = self._statusVar1)
		self._statusField1.grid(row = 6, column = 7, columnspan = 5)

		# Add the status field for trumps suit
		self._statusVar2 = StringVar()
		self._statusField2 = Entry(self, width = 20, textvariable = self._statusVar2)
		self._statusField2.grid(row = 8, column = 7, columnspan = 5)

		self._playerVar = Label(self, text="Player")
		self._playerVar.grid(row = 9, column = 0, columnspan = 5)

		# Add the status field for player score
		self._playerScore = StringVar()
		self._playerScoreField = Entry(self, width = 3, textvariable = self._playerScore)
		self._playerScoreField.grid(row = 9, column = 3, columnspan = 1)

		self._statusVar3 = StringVar()
		self._gameResult = Entry(self, width = 20, textvariable = self._statusVar3)
		self._gameResult.grid(row = 14, column = 0, columnspan = 5)

		self._newGame()

	def play_card(self, card_index):
		card = self._model.getPlayerCards()[card_index]
		print(f"Player selected card: {card}")

		# TODO: Add your game logic to validate and process this card play
		# Example:
		# if self._model.isValidPlay(card):
		#     self._model.playCard(card)
		#     self.update_board()
		#     self._playerButtons[card_index]['state'] = DISABLED
		#self._model.playCard(card)
		self._playerButtons[card_index]['state'] = DISABLED
		
	# Create the event handler methods
	def _newGame(self):
		"""Instantiates the model and establishes the GUI"""
		self._model = CardGame()

		global playerScore
		global computerScore
		global num_dealt_cards
		playerScore = 0
		computerScore = 0
		num_dealt_cards = 5
		
		# Refresh the card panes
		# Player Cards
		self._playerButtons = []
		self._playerImages = list(map(lambda card: PhotoImage(file=card.getFilename()), self._model.getPlayerCards()))
		player_cards = self._model.getPlayerCards()

		for i in range(5):
			btn = Button(self,image=self._playerImages[i],state=ACTIVE,command=lambda idx=i: self.play_card(idx))
			btn.grid(row=10, column=i, columnspan=1)
			self._playerButtons.append(btn)

		# Computer Cards	
		self._computerImages = list(map(lambda card: PhotoImage(file = card.getFilename()), self._model.getComputerCards()))
		self._computerLabels = list(map(lambda i: Label(self._computerPane, image = i), self._computerImages))
		for col in range(len(self._computerLabels)):
			self._computerLabels[col].grid(row = 0, column = col)

		#Trump Card	
		self._trumpsImages = list(map(lambda card: PhotoImage(file = card.getFilename()), self._model.getTrumpCards()))
		self._trumpsLabels = list(map(lambda i: Label(self._trumpsPane, image = i), self._trumpsImages))
		for col in range(len(self._trumpsLabels)):
			self._trumpsLabels[col].grid(row = 0, column = col)
			
		self._statusVar1.set("")
		self._statusVar2.set("")
		self._statusVar3.set("")
		#self._model.RobCard()

		round1Rob = self._model.RobCard(num_dealt_cards)
		round1Trumps = self._model.TrumpsAre()

		for i in range(0,5):
			playerScore += self._model.getPoints(i)[0]
			computerScore += self._model.getPoints(i)[1]
			
		# crude card comparison
		if playerScore ==25:
			result = "Congratulations! You win!"
		elif computerScore ==25:
			result = "Hard luck. Computer Wins."
		else:
			result = "Deal again!"

		self._statusVar1.set(round1Rob)
		self._statusVar2.set(round1Trumps)
		self._statusVar3.set(result)
		self._playerScore.set(playerScore)
		self._computerScore.set(computerScore)

		# Create the event handler methods
	def _dealAgain(self):
		"""Instantiates the model and establishes the GUI"""
		self._model = CardGame()

		global playerScore
		global computerScore
		global num_dealt_cards
		num_dealt_cards = num_dealt_cards + 5

		# Refresh the card panes
		# Player Cards
		self._playerButtons = []
		self._playerImages = list(map(lambda card: PhotoImage(file=card.getFilename()), self._model.getPlayerCards()))
		player_cards = self._model.getPlayerCards()

		for i in range(5):
			btn = Button(self,image=self._playerImages[i],state=ACTIVE,command=lambda idx=i: self.play_card(idx))
			btn.grid(row=10, column=i, columnspan=1)
			self._playerButtons.append(btn)

		# Computer Cards	
		self._computerImages = list(map(lambda card: PhotoImage(file = card.getFilename()), self._model.getComputerCards()))
		self._computerLabels = list(map(lambda i: Label(self._computerPane, image = i), self._computerImages))
		for col in range(len(self._computerLabels)):
			self._computerLabels[col].grid(row = 0, column = col)

		# Trump Card	
		self._trumpsImages = list(map(lambda card: PhotoImage(file = card.getFilename()), self._model.getTrumpCards()))
		self._trumpsLabels = list(map(lambda i: Label(self._trumpsPane, image = i), self._trumpsImages))
		for col in range(len(self._trumpsLabels)):
			self._trumpsLabels[col].grid(row = 0, column = col)
			
		self._statusVar1.set("")
		self._statusVar2.set("")
		self._statusVar3.set("")
		# self._model.RobCard()

		roundRob = self._model.RobCard(num_dealt_cards)
		roundTrumps = self._model.TrumpsAre()

		for i in range(0,5):
			while True:
				if playerScore < 25 and computerScore < 25:
					playerScore += self._model.getPoints(i)[0]
					computerScore += self._model.getPoints(i)[1]
				else:
					break
		if playerScore ==25:
			result = "Congratulations! You win!"
		else:
			result = "Hard luck. Computer Wins."			

		self._statusVar1.set(roundRob)
		self._statusVar2.set(roundTrumps)
		self._statusVar3.set(result)
		self._playerScore.set(playerScore)
		self._computerScore.set(computerScore)
		
def main():
	TwentyFiveGUI().mainloop()
	
main()
