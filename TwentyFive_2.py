"""
File: TwentyFive.py
Author: Paul Moran
Establishes a player class, dealer class, and game mechanics for a 25 card game.
"""

from cards import Deck, Card

class Player(object):
	"""This class represents a player in the 25 game."""	
	def __init__(self, cards):
		self._cards = cards
		for card in self._cards:
			card.turn()

	def __str__(self):
		"""Returns string rep of cards and points."""
		result = ", ".join(map(str, self._cards))
		result += "\n  " + str(self.getPoints()) + " points"
		return result
		
	def getCards(self):
		return self._cards

class Computer(Player):
	def __init__(self, cards):
		""" Conceal the computer's hand of cards"""
		Player.__init__(self, cards)
		self._showOneCard = True
		#for card in self._cards:
		#	card.turn()
		
	def __str__(self):
		"""Return just one card if not hit yet."""
		if self._showOneCard:
			return str(self._cards[0])
		else:
			return Player.__str__(self)

class Trumps(Player):
	def __init__(self, cards):
		"""show card"""
		Player.__init__(self, cards)

class CardGame(object):
	def __init__(self):
		self._deck = Deck()
		self._deck.shuffle()
		
		#Pass the player and the computer 3 cards each, follwed by 2 cards each
		# First deal of 3 cards each
		player_deal1 = [self._deck.deal(), self._deck.deal(), self._deck.deal()]
		computer_deal1 = [self._deck.deal(), self._deck.deal(), self._deck.deal()]

		# Second deal of 2 cards each
		player_deal2 = [self._deck.deal(), self._deck.deal()]
		computer_deal2 = [self._deck.deal(), self._deck.deal()]

		self._player = Player(player_deal1 + player_deal2)
		self._computer = Computer(computer_deal1 + computer_deal2)

		# The card at the top of the deck becomes the trump card
		self._trumps = Trumps([self._deck.deal()])

	def TrumpsAre(self):
		if self._trumps._cards[0].suit == "Spades":
			return "Trumps are Spades!"
		elif self._trumps._cards[0].suit == "Clubs":
			return "Trumps are Clubs!"
		elif self._trumps._cards[0].suit == "Hearts":
			return "Trumps are Hearts!"
		elif self._trumps._cards[0].suit == "Diamonds":
			return "Trumps are Diamonds!"

	def getPlayerCards(self):
		"""Returns a list of the player's cards."""
		return self._player.getCards()
		
	def getComputerCards(self):
		"""Returns a list of the computer's cards."""
		return self._computer.getCards()

	def getTrumpCards(self):
		"""Returns a list of the trump card."""
		return self._trumps.getCards()

	def RobCard(self):
		""" checks to see who has the rob"""
		if (self._trumps._cards[0].rank == 1):
			return "Turned an Ace - you can rob!"
		for i in range(0,5):
			if self._player._cards[i].rank == 1  and self._trumps._cards[0].suit == self._player._cards[i].suit:
				return "Congrats, you have the rob!"
			elif self._computer._cards[i].rank == 1 and self._trumps._cards[0].suit == self._computer._cards[i].suit:
				return "The computer has the rob!"

	def getPoints(self):
		"""Returns the points scored by player"""
		player_count = 0
		computer_count = 0

		#for card in self._cards:
		for i in range(0,5):
			if self._trumps._cards[0].suit == "Spades":
				if self._player._cards[i].suit == "Spades" and self._computer._cards[i].suit == "Spades":
					if val_list_trump_spades.index(self._player._cards[i].rank) > val_list_trump_spades.index(self._computer._cards[i].rank):
						player_count += 5
					else:
						computer_count += 5

				elif self._player._cards[i].suit == "Spades" and self._computer._cards[i].suit != "Spades":
					if (self._player._cards[i].rank != 5 or self._player._cards[i].rank != 11) and (self._computer._cards[i].suit == "Hearts" and self._computer._cards[i].rank == 1):
						computer_count += 5
					else:
						player_count += 5
				elif self._player._cards[i].suit != "Spades" and self._computer._cards[i].suit == "Spades":
					if (self._player._cards[i].suit == "Hearts" and self._player._cards[i].rank == 1) and (self._computer._cards[i].rank != 5 or self._computer._cards[i].rank != 11):
						player_count += 5
					else:
						computer_count += 5

				elif self._player._cards[i].suit != "Spades" and self._computer._cards[i].suit != "Spades":
					if self._player._cards[i].suit == "Clubs" and self._computer._cards[i].suit == "Clubs":
						if val_list_clubs.index(self._player._cards[i].rank) > val_list_clubs.index(self._computer._cards[i].rank):
							player_count += 5
						else:
							computer_count += 5
					elif self._player._cards[i].suit == "Clubs" and self._computer._cards[i].suit != "Clubs":
						player_count += 5

					elif self._player._cards[i].suit == "Hearts" and self._computer._cards[i].suit == "Hearts":
						if self._player._cards[i].suit == "Hearts" and self._player._cards[i].rank == 1:
							player_count += 5
						elif self._computer._cards[i].suit == "Hearts" and self._computer._cards[i].rank == 1:
							computer_count += 5
						else:
							if val_list_hearts.index(self._player._cards[i].rank) > val_list_hearts.index(self._computer._cards[i].rank):
								player_count += 5
							else:
								computer_count += 5
					elif self._player._cards[i].suit == "Hearts" and self._computer._cards[i].suit != "Hearts":
						player_count += 5

					elif self._player._cards[i].suit == "Diamonds" and self._computer._cards[i].suit == "Diamonds":
						if val_list_diamonds.index(self._player._cards[i].rank) > val_list_diamonds.index(self._computer._cards[i].rank):
							player_count += 5
						else:
							computer_count += 5
					elif self._player._cards[i].suit == "Diamonds" and self._computer._cards[i].suit != "Diamonds":
						player_count += 5

			elif self._trumps._cards[0].suit == "Clubs":
				if self._player._cards[i].suit == "Clubs" and self._computer._cards[i].suit == "Clubs":
					if val_list_trump_clubs.index(self._player._cards[i].rank) > val_list_trump_clubs.index(self._computer._cards[i].rank):
						player_count += 5
					else:
						computer_count += 5

				elif self._player._cards[i].suit == "Clubs" and self._computer._cards[i].suit != "Clubs":
					if (self._player._cards[i].rank != 5 or self._player._cards[i].rank != 11) and (self._computer._cards[i].suit == "Hearts" and self._computer._cards[i].rank == 1):
						computer_count += 5
					else:
						player_count += 5
				elif self._player._cards[i].suit != "Clubs" and self._computer._cards[i].suit == "Clubs":
					if (self._player._cards[i].suit == "Hearts" and self._player._cards[i].rank == 1) and (self._computer._cards[i].rank != 5 or self._computer._cards[i].rank != 11):
						player_count += 5
					else:
						computer_count += 5

				elif self._player._cards[i].suit != "Clubs" and self._computer._cards[i].suit != "Clubs":
					if self._player._cards[i].suit == "Spades" and self._computer._cards[i].suit == "Spades":
						if val_list_spades.index(self._player._cards[i].rank) > val_list_spades.index(self._computer._cards[i].rank):
							player_count += 5
						else:
							computer_count += 5
					elif self._player._cards[i].suit == "Spades" and self._computer._cards[i].suit != "Spades":
						player_count += 5

					elif self._player._cards[i].suit == "Hearts" and self._computer._cards[i].suit == "Hearts":
						if self._player._cards[i].suit == "Hearts" and self._player._cards[i].rank == 1:
							player_count += 5
						elif self._computer._cards[i].suit == "Hearts" and self._computer._cards[i].rank == 1:
							computer_count += 5
						else:
							if val_list_hearts.index(self._player._cards[i].rank) > val_list_hearts.index(self._computer._cards[i].rank):
								player_count += 5
							else:
								computer_count += 5
					elif self._player._cards[i].suit == "Hearts" and self._computer._cards[i].suit != "Hearts":
						player_count += 5

					elif self._player._cards[i].suit == "Diamonds" and self._computer._cards[i].suit == "Diamonds":
						if val_list_diamonds.index(self._player._cards[i].rank) > val_list_diamonds.index(self._computer._cards[i].rank):
							player_count += 5
						else:
							computer_count += 5
					elif self._player._cards[i].suit == "Diamonds" and self._computer._cards[i].suit != "Diamonds":
						player_count += 5

			elif self._trumps._cards[0].suit == "Hearts":
				if self._player._cards[i].suit == "Hearts" and self._computer._cards[i].suit == "Hearts":
					if val_list_trump_hearts.index(self._player._cards[i].rank) > val_list_trump_hearts.index(self._computer._cards[i].rank):
						player_count += 5
					else:
						computer_count += 5
				elif self._player._cards[i].suit == "Hearts" and self._computer._cards[i].suit != "Hearts":
					player_count += 5

				elif self._player._cards[i].suit != "Hearts" and self._computer._cards[i].suit == "Hearts":
					computer_count += 5

				elif self._player._cards[i].suit != "Hearts" and self._computer._cards[i].suit != "Hearts":
					if self._player._cards[i].suit == "Spades" and self._computer._cards[i].suit == "Spades":
						if val_list_spades.index(self._player._cards[i].rank) > val_list_spades.index(self._computer._cards[i].rank):
							player_count += 5
						else:
							computer_count += 5
					elif self._player._cards[i].suit == "Spades" and self._computer._cards[i].suit != "Spades":
						player_count += 5

					if self._player._cards[i].suit == "Clubs" and self._computer._cards[i].suit == "Clubs":
						if val_list_clubs.index(self._player._cards[i].rank) > val_list_clubs.index(self._computer._cards[i].rank):
							player_count += 5
						else:
							computer_count += 5

					elif self._player._cards[i].suit == "Clubs" and self._computer._cards[i].suit != "Clubs":
						player_count += 5

					if self._player._cards[i].suit == "Diamonds" and self._computer._cards[i].suit == "Diamonds":
						if val_list_diamonds.index(self._player._cards[i].rank) > val_list_diamonds.index(self._computer._cards[i].rank):
							player_count += 5
						else:
							computer_count += 5
					elif self._player._cards[i].suit == "Diamonds" and self._computer._cards[i].suit != "Diamonds":
						player_count += 5

			elif self._trumps._cards[0].suit == "Diamonds":
				if self._player._cards[i].suit == "Diamonds" and self._computer._cards[i].suit == "Diamonds":
					if val_list_trump_diamonds.index(self._player._cards[i].rank) > val_list_trump_diamonds.index(self._computer._cards[i].rank):
						player_count += 5
					else:
						computer_count += 5

				elif self._player._cards[i].suit == "Diamonds" and self._computer._cards[i].suit != "Diamonds":
					if (self._player._cards[i].rank != 5 or self._player._cards[i].rank != 11) and (self._computer._cards[i].suit == "Hearts" and self._computer._cards[i].rank == 1):
						computer_count += 5
					else:
						player_count += 5
				elif self._player._cards[i].suit != "Diamonds" and self._computer._cards[i].suit == "Diamonds":
					if (self._player._cards[i].suit == "Hearts" and self._player._cards[i].rank == 1) and (self._computer._cards[i].rank != 5 or self._computer._cards[i].rank != 11):
						player_count += 5
					else:
						computer_count += 5

				elif self._player._cards[i].suit != "Diamonds" and self._computer._cards[i].suit != "Diamonds":
					if self._player._cards[i].suit == "Spades" and self._computer._cards[i].suit == "Spades":
						if val_list_spades.index(self._player._cards[i].rank) > val_list_spades.index(self._computer._cards[i].rank):
							player_count += 5
						else:
							computer_count += 5

					elif self._player._cards[i].suit == "Spades" and self._computer._cards[i].suit != "Spades":
						player_count += 5

					elif self._player._cards[i].suit == "Clubs" and self._computer._cards[i].suit == "Clubs":
						if val_list_clubs.index(self._player._cards[i].rank) > val_list_clubs.index(self._computer._cards[i].rank):
							player_count += 5
						else:
							computer_count += 5

					elif self._player._cards[i].suit == "Clubs" and self._computer._cards[i].suit != "Clubs":
						player_count += 5

					elif self._player._cards[i].suit == "Hearts" and self._computer._cards[i].suit == "Hearts":
						if self._player._cards[i].suit == "Hearts" and self._player._cards[i].rank == 1:
							player_count += 5
						elif self._computer._cards[i].suit == "Hearts" and self._computer._cards[i].rank == 1:
							computer_count += 5
						else:
							if val_list_hearts.index(self._player._cards[i].rank) > val_list_hearts.index(self._computer._cards[i].rank):
								player_count += 5
							else:
								computer_count += 5
					elif self._player._cards[i].suit == "Hearts" and self._computer._cards[i].suit != "Hearts":
						player_count += 5

		# crude card comparison
		if player_count > computer_count:
			result = "Congratulations! You win!"
		else:
			result = "Hard luck. Computer Wins"
		return player_count, computer_count, result

	""" Defines the rules and rankings of cards """
Rank_Trump_Spades = {1: 10, 2: 9, 3: 8, 4: 7, 5: 6, 6: 4, 7: 3, 8: 2, 9: 12, 10: 13, 11: 1, 12: 11, 13: 5}
Rank_Trump_Clubs = {1: 10, 2: 9, 3: 8, 4: 7, 5: 6, 6: 4, 7: 3, 8: 2, 9: 12, 10: 13, 11: 1, 12: 11, 13: 5}
Rank_Trump_Hearts = {1: 2, 2: 3, 3: 4, 4: 6, 5: 7, 6: 8, 7: 9, 8: 10, 9: 12, 10: 13, 11: 1, 12: 11, 13: 5}
Rank_Trump_Diamonds = {1: 2, 2: 3, 3: 4, 4: 6, 5: 7, 6: 8, 7: 9, 8: 10, 9: 12, 10: 13, 11: 1, 12: 11, 13: 5}

Rank_Spades = {1: 10, 2: 9, 3: 8, 4: 7, 5: 6, 6: 5, 7: 4, 8: 3, 9: 2, 10: 1, 11: 11, 12: 12, 13: 13}
Rank_Clubs = {1: 10, 2: 9, 3: 8, 4: 7, 5: 6, 6: 5, 7: 4, 8: 3, 9: 2, 10: 1, 11: 11, 12: 12, 13: 13}
Rank_Hearts = {1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7, 7: 8, 8: 9, 9: 10, 10: 1, 11: 11, 12: 12, 13: 13}
Rank_Diamonds = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, 11: 11, 12: 12, 13: 13}
 
# list out keys and values separately
key_list_trump_spades = list(Rank_Trump_Spades.keys())
val_list_trump_spades = list(Rank_Trump_Spades.values())

key_list_trump_clubs = list(Rank_Trump_Clubs.keys())
val_list_trump_clubs = list(Rank_Trump_Clubs.values())

key_list_trump_hearts = list(Rank_Trump_Hearts.keys())
val_list_trump_hearts = list(Rank_Trump_Hearts.values())

key_list_trump_diamonds = list(Rank_Trump_Diamonds.keys())
val_list_trump_diamonds = list(Rank_Trump_Diamonds.values())

key_list_spades = list(Rank_Spades.keys())
val_list_spades = list(Rank_Spades.values())

key_list_clubs = list(Rank_Clubs.keys())
val_list_clubs = list(Rank_Clubs.values())

key_list_hearts = list(Rank_Hearts.keys())
val_list_hearts = list(Rank_Hearts.values())

key_list_diamonds = list(Rank_Diamonds.keys())
val_list_diamonds = list(Rank_Diamonds.values())
