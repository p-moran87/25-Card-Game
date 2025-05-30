"""
File: 25_game_gui.py
Author: Paul Moran

GUI based version of the 25 card game
"""

from tkinter import *
from TwentyFive_2 import CardGame
from cards import Deck, Card
#from PIL import Image, ImageTk
import os


class TwentyFiveGUI(Frame):

	def __init__(self):
		Frame.__init__(self, bg='darkgreen')
		self.master.title("TwentyFive")
		self.master.configure(bg='darkgreen')
		self.master.geometry("800x600")
		self.grid()

		self._dealer = "player"  # or "computer"
		
		self._newGameButton = Button(self, text = "New Game", command = self._newGame)
		self._newGameButton.grid(row = 0, column = 7)

		self._dealAgainButton = Button(self, text = "Deal Again", command = self._dealAgain) #self._dealAgain)
		self._dealAgainButton.grid(row = 1, column = 7)

		self._computerVar = Label(self, text="Computer")
		self._computerVar.grid(row = 2, column = 0, columnspan = 5)

		self._computerScore = StringVar()
		self._computerScoreField = Entry(self, width = 3, textvariable = self._computerScore)
		self._computerScoreField.grid(row = 2, column = 3, columnspan = 1)

		# Add the panes for the player and computer cards
		self._hiddenPane = Frame(self)
		self._hiddenPane.grid(row = 0, column = 0, columnspan = 5)

		self._computerPane = Frame(self)
		self._computerPane.grid(row = 1, column = 0, columnspan = 5)

		self._playerPane = Frame(self)
		self._playerPane.grid(row = 15, column=0, columnspan=5)

		# Add the status field for robbing
		self._statusVar1 = StringVar()
		self._statusField1 = Entry(self, width = 25, textvariable = self._statusVar1)
		self._statusField1.grid(row = 6, column = 7, columnspan = 10)

		# trumps pane
		self._trumpsPane = Frame(self)
		self._trumpsPane.grid(row = 7, column = 0, columnspan = 10)

		# Add the status field for trumps suit
		self._statusVar2 = StringVar()
		self._statusField2 = Entry(self, width = 20, textvariable = self._statusVar2)
		self._statusField2.grid(row = 8, column = 7, columnspan = 10)

		self._playerVar = Label(self, text="Player")
		self._playerVar.grid(row = 9, column = 0, columnspan = 5)

		# Add the status field for player score
		self._playerScore = StringVar()
		self._playerScoreField = Entry(self, width = 3, textvariable = self._playerScore)
		self._playerScoreField.grid(row = 9, column = 3, columnspan = 1)

		self._statusVar3 = StringVar()
		self._gameResult = Entry(self, width = 30, textvariable = self._statusVar3)
		self._gameResult.grid(row = 35, column = 0, columnspan = 5)

		self._computer_played_indices = []

		self._newGame()

		#Rank_Trump_Spades = {1: 10, 2: 9, 3: 8, 4: 7, 5: 6, 6: 4, 7: 3, 8: 2, 9: 12, 10: 13, 11: 1, 12: 11, 13: 5}
		#Rank_Trump_Clubs = {1: 10, 2: 9, 3: 8, 4: 7, 5: 6, 6: 4, 7: 3, 8: 2, 9: 12, 10: 13, 11: 1, 12: 11, 13: 5}
		#Rank_Trump_Hearts = {1: 2, 2: 3, 3: 4, 4: 6, 5: 7, 6: 8, 7: 9, 8: 10, 9: 12, 10: 13, 11: 1, 12: 11, 13: 5}
		#Rank_Trump_Diamonds = {1: 2, 2: 3, 3: 4, 4: 6, 5: 7, 6: 8, 7: 9, 8: 10, 9: 12, 10: 13, 11: 1, 12: 11, 13: 5}

		self.trump_rankings = {
			'Spades': {
				5: 13,		# Highest
				11: 12,		# Jack
				('Hearts', 1): 11,		# Ace of Hearts
				1: 10,		# Ace of Spades (normal)
				13: 9, 12: 8, 2: 7, 3: 6, 4: 5, 6: 4, 7: 3, 8: 2, 9: 1, 10: 0
			},
			'Clubs': {
				5: 13, 11: 12,('Hearts', 1): 11, 1: 10,
				13: 9, 12: 8, 2: 7, 3: 6, 4: 5, 6: 4, 7: 3, 8: 2, 9: 1, 10: 0
			},
			'Hearts': {
				5: 13, 11: 12,
				1: 11,	# Ace of Hearts is already in suit
				13: 10, 12: 9, 10: 8, 9: 7, 8: 6, 7: 5, 6: 4, 4: 3, 3: 2, 2: 1
			},
			'Diamonds': {
				5: 13, 11: 12,('Hearts', 1): 11, 1: 10,
				13: 8, 12: 8, 10: 7, 9: 6, 8: 5, 7: 4, 6: 3, 4: 2, 3: 1, 2: 0
			}
		}

		self.suit_rankings = {
			"Spades": {13: 13, 12: 12, 11: 11, 1: 10, 2: 9, 3: 8, 4: 7, 5: 6, 6: 5, 7: 4, 8: 3, 9: 2, 10: 1},
			"Clubs": {13: 13, 12: 12, 11: 11, 1: 10, 2: 9, 3: 8, 4: 7, 5: 6, 6: 5, 7: 4, 8: 3, 9: 2, 10: 1},

			"Hearts": {1: 13, 13: 12, 12: 11, 10: 10, 9: 9, 8: 8, 7: 7, 6: 6, 5: 5, 4: 4, 3: 3, 2: 2},
			"Diamonds": {13: 13, 12: 12, 11: 11, 10: 10, 9: 9, 8: 8, 7: 7, 6: 6, 5: 5, 4: 4, 3: 3, 2: 2, 1: 1}
			}

	def _get_card_strength(self, card, trump_suit):
		if card is None:
			return -1  # or some sentinel value lower than any real card's strength

		# Special case: Ace of Hearts is ALWAYS the 3rd highest trump
		if card.suit == "Hearts" and card.rank == 1:
			# Temporarily treat it as a trump card for strength
			return self.trump_rankings[trump_suit].get(('Hearts', 1), 0)

		# Normal trump card
		if card.suit == trump_suit:
			return self.trump_rankings[trump_suit].get((card.suit, card.rank), 0)

		# Non-trump card
		return self.suit_rankings.get(card.suit, {}).get(card.rank, 0)

	def _choose_computer_card(self, lead_card, trump_suit, computer_hand):
		computer_hand = [card for i, card in enumerate(computer_hand) if i not in self._computer_played_indices]
		
		if lead_card is None:
			# Computer is leading: play strongest trump if available, otherwise strongest card
			trump_cards = [card for card in computer_hand if card.suit == trump_suit]
			if trump_cards:
				return max(trump_cards, key=lambda c: self._get_card_strength(c, trump_suit))
			return max(computer_hand, key=lambda c: self._get_card_strength(c, trump_suit))

		lead_is_trump = (lead_card.suit == trump_suit)
		lead_strength = self._get_card_strength(lead_card, trump_suit)

		if lead_is_trump:
			# Player led with a trump
			computer_trumps = [card for card in computer_hand if card.suit == trump_suit]
			if computer_trumps:
				beating_trumps = [card for card in computer_trumps
									if self._get_card_strength(card, trump_suit) > lead_strength]
				if beating_trumps:
					return min(beating_trumps, key=lambda c: self._get_card_strength(c, trump_suit))
				return min(computer_trumps, key=lambda c: self._get_card_strength(c, trump_suit))
			return min(computer_hand, key=lambda c: self._get_card_strength(c, trump_suit))

		else:
			# Player led with a non-trump
			computer_trumps = [card for card in computer_hand if card.suit == trump_suit]
			if computer_trumps:
				return min(computer_trumps, key=lambda c: self._get_card_strength(c, trump_suit))

			same_suit_cards = [card for card in computer_hand if card.suit == lead_card.suit]
			beating_same_suit = [card for card in same_suit_cards
						if self._get_card_strength(card, trump_suit) > lead_strength]
			if beating_same_suit:
				return min(beating_same_suit, key=lambda c: self._get_card_strength(c, trump_suit))

			return min(computer_hand, key=lambda c: self._get_card_strength(c, trump_suit))
	
	def _computer_leads(self):
		# Computer leads the trick
		trump_suit = self._model.getTrumpCards()[0].suit
		computer_hand = self._model.getComputerCards()

		comp_card = self._choose_computer_card(lead_card=None, trump_suit=trump_suit, computer_hand=computer_hand)
		self.comp_card = comp_card  # store for later comparison

		# Find the index of the card to remove/disable it later
		full_computer_hand = self._model.getComputerCards()
		comp_card_index = full_computer_hand.index(comp_card)
		self._computer_played_indices.append(comp_card_index)

		print("Computer hand:", computer_hand)
		print("Computer played:", comp_card)
		print("Index of played card:", comp_card_index)

		# Remove the back card label (hides it visually)
		self._backCardLabels[comp_card_index].grid_forget()

		# Place the real card in the same grid cell (same row/column)
		self._computerLabels[comp_card_index].grid(row=1, column=comp_card_index)

		self._statusVar3.set("Computer has played. Your turn.")

	def _play_card(self, card_index):
		global p1_card
		global comp_card
		global playerScore
		global computerScore

		player_hand = self._model.getPlayerCards()
		computer_hand = self._model.getComputerCards()
		trump_suit = self._model.getTrumpCards()[0].suit

		if self.lead_player == "computer":
			# Computer already led
			comp_card = self.comp_card  # from earlier call to _computer_leads()
			p1_card = player_hand[card_index]
			led_by = "computer"

		else:
			# Player leads
			p1_card = player_hand[card_index]
			comp_card = self._choose_computer_card(lead_card=p1_card, trump_suit=trump_suit, computer_hand=computer_hand)
			led_by = "player"

			full_computer_hand = self._model.getComputerCards()
			comp_index = full_computer_hand.index(comp_card)
			self._computer_played_indices.append(comp_index)

			self._backCardLabels[comp_index].grid_forget()
			self._computerLabels[comp_index].grid(row=1, column=comp_index)

		# Disable the player's button
		self._playerButtons[card_index]['state'] = DISABLED
		self._playerLabels[card_index].grid(row=20, column=card_index)

		# Get points
		p_points, c_points = self._model.getPoints(p1_card, comp_card, led_by=led_by)
		playerScore += p_points
		computerScore += c_points

		# Decide who leads next
		if p_points > c_points:
			self.lead_player = "player"
		elif c_points > p_points:
			self.lead_player = "computer"

		# Update GUI scores
		self._playerScore.set(playerScore)
		self._computerScore.set(computerScore)

		# Check for win condition
		if playerScore >= 25:
			self._statusVar3.set("Congratulations! You win!")
			self._disable_remaining_buttons()
		elif computerScore >= 25:
			self._statusVar3.set("Hard luck. Computer Wins.")
			self._disable_remaining_buttons()
		elif playerScore + computerScore < 25:
			if self.lead_player == "computer":
				self._computer_leads()
			else:
				self._statusVar3.set("Your turn to lead.")
		else:
			self._statusVar3.set("Deal again!.")

	def _disable_remaining_buttons(self):
		for btn in self._playerButtons:
			btn['state'] = DISABLED
		
	def _refresh_cards(self):
		"""Instantiates the model and establishes the GUI"""
		global num_dealt_cards

		self._model = CardGame()

		# Refresh the card panes
		# Player Cards
		self._playerImages = list(map(lambda card: PhotoImage(file=card.getFilename()), self._model.getPlayerCards()))
		self._playerLabels = list(map(lambda i: Label(self._playerPane, image = i), self._playerImages))

		player_cards = self._model.getPlayerCards()

		# Computer Cards
		computer_cards = self._model.getComputerCards()
		self._computerImages = list(map(lambda card: PhotoImage(file = card.getFilename()), self._model.getComputerCards()))
		self._computerLabels = list(map(lambda i: Label(self._computerPane, image = i), self._computerImages))

		# Absolute image path
		photo = PhotoImage(file = "DECK/b.gif")
		self._backCardLabels = []
		
		# hidden Cards
		for i in range(5):
			panel = Label(self._hiddenPane, image=photo)
			panel.image = photo
			panel.grid(row=0, column=i)
			self._backCardLabels.append(panel)

		#Trump Card	
		self._trumpsImages = list(map(lambda card: PhotoImage(file = card.getFilename()), self._model.getTrumpCards()))
		self._trumpsLabels = list(map(lambda i: Label(self._trumpsPane, image = i), self._trumpsImages))
		for col in range(len(self._trumpsLabels)):
			self._trumpsLabels[col].grid(row = 3, column = col)

		roundRob = self._model.RobCard(num_dealt_cards)
		roundTrumps = self._model.TrumpsAre()
		#self._model.RobCard()

		self._statusVar1.set(roundRob)
		self._statusVar2.set(roundTrumps)
		self._statusVar3.set("")

	# Create the event handler methods
	def _newGame(self):
		global playerScore
		global computerScore
		global num_dealt_cards

		playerScore = 0
		computerScore = 0
		num_dealt_cards = 5

		self.lead_player = "player"

		self._refresh_cards()
		self._setup_card_buttons()

		self._computer_played_indices = []

		self._playerScore.set(playerScore)
		self._computerScore.set(computerScore)
		self._statusVar3.set("Please select a card to play.")

	def _dealAgain(self):
		global num_dealt_cards

		self._computer_played_indices = []

		if playerScore >= 25 or computerScore >= 25:
			self._statusVar3.set("Game is over. Start a new game.")
			return

		num_dealt_cards += 5
		self._refresh_cards()
		self._setup_card_buttons()
		self._statusVar3.set("New round! Please select a card to play.")

	def _setup_card_buttons(self):
		self._playerButtons = []

		for i in range(5):
			btn = Button(self, image=self._playerImages[i], state=ACTIVE, command=lambda idx=i: self._play_card(idx))
			btn.grid(row=30, column=i, columnspan=1)
			self._playerButtons.append(btn)
		
def main():
	TwentyFiveGUI().mainloop()
	
main()
