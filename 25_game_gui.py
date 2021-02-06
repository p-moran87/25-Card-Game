"""
File: 25_game_gui.py
Author: Paul

GUI based version of the 25 card game
"""

from tkinter import *
from TwentyFive import CardGame

class TwentyFiveGUI(Frame):

	def __init__(self):
		Frame.__init__(self, bg='darkgreen')
		self.master.title("TwentyFive")
		self.master.configure(bg='darkgreen')
		self.master.geometry("800x600")
		self.grid()
		
		#Add the command buttons
		#self._hitButton = Button(self, text = "Hit", command = self._hit)
		#self._hitButton.grid(row = 0, column = 0)
		#self._passButton = Button(self, text = "Pass", command = self._pass)
		#self._passButton.grid(row = 0, column = 1)
		
		self._newGameButton = Button(self, text = "New Game", command = self._newGame)
		self._newGameButton.grid(row = 0, column = 7)

		self._computerVar = Label(self, text="Computer")
		self._computerVar.grid(row = 1, column = 0, columnspan = 5)

		self._computerScore = StringVar()
		self._computerScoreField = Entry(self, width = 3, textvariable = self._computerScore)
		self._computerScoreField.grid(row = 1, column = 3, columnspan = 1)

		#Add the panes for the player and dealer cards
		self._computerPane = Frame(self)
		self._computerPane.grid(row = 3, column = 0, columnspan = 5)

		self._trumpsPane = Frame(self)
		self._trumpsPane.grid(row = 7, column = 0, columnspan = 5)

		#Add the status field for robbing
		self._statusVar1 = StringVar()
		self._statusField1 = Entry(self, width = 20, textvariable = self._statusVar1)
		self._statusField1.grid(row = 6, column = 7, columnspan = 5)

		#Add the status field for trumps suit
		self._statusVar2 = StringVar()
		self._statusField2 = Entry(self, width = 20, textvariable = self._statusVar2)
		self._statusField2.grid(row = 8, column = 7, columnspan = 5)

		self._playerVar = Label(self, text="Player")
		self._playerVar.grid(row = 9, column = 0, columnspan = 5)

		#Add the status field for player score
		self._playerScore = StringVar()
		self._playerScoreField = Entry(self, width = 3, textvariable = self._playerScore)
		self._playerScoreField.grid(row = 9, column = 3, columnspan = 1)

		self._playerPane = Frame(self)
		self._playerPane.grid(row = 10, column = 0, columnspan = 5)

		self._playerCard1 = Button(self, text = "Card 1", state=DISABLED)
		self._playerCard1.grid(row = 11, column = 0)
		self._playerCard2 = Button(self, text = "Card 2", state=DISABLED)
		self._playerCard2.grid(row = 11, column = 1)
		self._playerCard3 = Button(self, text = "Card 3", state=DISABLED)
		self._playerCard3.grid(row = 11, column = 2)
		self._playerCard4 = Button(self, text = "Card 4", state=DISABLED)
		self._playerCard4.grid(row = 11, column = 3)
		self._playerCard5 = Button(self, text = "Card 5", state=DISABLED)
		self._playerCard5.grid(row = 11, column = 4)

		self._statusVar3 = StringVar()
		self._gameResult = Entry(self, width = 20, textvariable = self._statusVar3)
		self._gameResult.grid(row = 14, column = 0, columnspan = 5)

		self._newGame()
		
	# Create the event handler methods
	def _newGame(self):
		"""Instantiates the model and establishes the GUI"""
		self._model = CardGame()
		
		#Refresh the card panes
		#Player Cards
		self._playerImages = list(map(lambda card: PhotoImage(file = card.getFilename()), self._model.getPlayerCards()))
		self._playerLabels = list(map(lambda i: Label(self._playerPane, image = i), self._playerImages))
		for col in range(len(self._playerLabels)):
			self._playerLabels[col].grid(row = 0, column = col)
			
		#Dealer Cards	
		self._computerImages = list(map(lambda card: PhotoImage(file = card.getFilename()), self._model.getComputerCards()))
		self._computerLabels = list(map(lambda i: Label(self._computerPane, image = i), self._computerImages))
		for col in range(len(self._computerLabels)):
			self._computerLabels[col].grid(row = 0, column = col)

		#Trump Card	
		self._trumpsImages = list(map(lambda card: PhotoImage(file = card.getFilename()), self._model.getTrumpCards()))
		self._trumpsLabels = list(map(lambda i: Label(self._trumpsPane, image = i), self._trumpsImages))
		for col in range(len(self._trumpsLabels)):
			self._trumpsLabels[col].grid(row = 0, column = col)
			
		#Re-enable the buttons and clear the status field
		#self._hitButton["state"] = NORMAL
		#self._passButton["state"] = NORMAL
		self._statusVar1.set("")
		self._statusVar2.set("")
		self._statusVar3.set("")
		#self._model.RobCard()

		outcome1 = self._model.RobCard()
		outcome2 = self._model.TrumpsAre()
		outcome3 = self._model.getPoints()

		self._statusVar1.set(outcome1)
		self._statusVar2.set(outcome2)
		self._playerScore.set(outcome3[0])
		self._computerScore.set(outcome3[1])
		self._statusVar3.set(outcome3[2])
		
def main():
	TwentyFiveGUI().mainloop()
	
main()





