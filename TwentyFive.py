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
					if self.scoreTrumpSpades(self._player._cards[i]) > self.scoreTrumpSpades(self._computer._cards[i]):
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
						if self.scoreClubs(self._player._cards[i]) > self.scoreClubs(self._computer._cards[i]):
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
							if self.scoreHearts(self._player._cards[i]) > self.scoreHearts(self._computer._cards[i]):
								player_count += 5
							else:
								computer_count += 5
					elif self._player._cards[i].suit == "Hearts" and self._computer._cards[i].suit != "Hearts":
						player_count += 5

					elif self._player._cards[i].suit == "Diamonds" and self._computer._cards[i].suit == "Diamonds":
						if self.scoreDiamonds(self._player._cards[i]) > self.scoreDiamonds(self._computer._cards[i]):
							player_count += 5
						else:
							computer_count += 5
					elif self._player._cards[i].suit == "Diamonds" and self._computer._cards[i].suit != "Diamonds":
						player_count += 5

			elif self._trumps._cards[0].suit == "Clubs":
				if self._player._cards[i].suit == "Clubs" and self._computer._cards[i].suit == "Clubs":
					if self.scoreTrumpClubs(self._player._cards[i]) > self.scoreTrumpClubs(self._computer._cards[i]):
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
						if self.scoreSpades(self._player._cards[i]) > self.scoreSpades(self._computer._cards[i]):
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
							if self.scoreHearts(self._player._cards[i]) > self.scoreHearts(self._computer._cards[i]):
								player_count += 5
							else:
								computer_count += 5
					elif self._player._cards[i].suit == "Hearts" and self._computer._cards[i].suit != "Hearts":
						player_count += 5

					elif self._player._cards[i].suit == "Diamonds" and self._computer._cards[i].suit == "Diamonds":
						if self.scoreDiamonds(self._player._cards[i]) > self.scoreDiamonds(self._computer._cards[i]):
							player_count += 5
						else:
							computer_count += 5
					elif self._player._cards[i].suit == "Diamonds" and self._computer._cards[i].suit != "Diamonds":
						player_count += 5

			elif self._trumps._cards[0].suit == "Hearts":
				if self._player._cards[i].suit == "Hearts" and self._computer._cards[i].suit == "Hearts":
					if self.scoreTrumpHearts(self._player._cards[i]) > self.scoreTrumpHearts(self._computer._cards[i]):
						player_count += 5
					else:
						computer_count += 5
				elif self._player._cards[i].suit == "Hearts" and self._computer._cards[i].suit != "Hearts":
					player_count += 5

				elif self._player._cards[i].suit != "Hearts" and self._computer._cards[i].suit == "Hearts":
					computer_count += 5

				elif self._player._cards[i].suit != "Hearts" and self._computer._cards[i].suit != "Hearts":
					if self._player._cards[i].suit == "Spades" and self._computer._cards[i].suit == "Spades":
						if self.scoreSpades(self._player._cards[i]) > self.scoreSpades(self._computer._cards[i]):
							player_count += 5
						else:
							computer_count += 5
					elif self._player._cards[i].suit == "Spades" and self._computer._cards[i].suit != "Spades":
						player_count += 5

					if self._player._cards[i].suit == "Clubs" and self._computer._cards[i].suit == "Clubs":
						if self.scoreClubs(self._player._cards[i]) > self.scoreClubs(self._computer._cards[i]):
							player_count += 5
						else:
							computer_count += 5

					elif self._player._cards[i].suit == "Clubs" and self._computer._cards[i].suit != "Clubs":
						player_count += 5

					if self._player._cards[i].suit == "Diamonds" and self._computer._cards[i].suit == "Diamonds":
						if self.scoreDiamonds(self._player._cards[i]) > self.scoreDiamonds(self._computer._cards[i]):
							player_count += 5
						else:
							computer_count += 5
					elif self._player._cards[i].suit == "Diamonds" and self._computer._cards[i].suit != "Diamonds":
						player_count += 5

			elif self._trumps._cards[0].suit == "Diamonds":
				if self._player._cards[i].suit == "Diamonds" and self._computer._cards[i].suit == "Diamonds":
					if self.scoreTrumpDiamonds(self._player._cards[i]) > self.scoreTrumpDiamonds(self._computer._cards[i]):
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
						if self.scoreSpades(self._player._cards[i]) > self.scoreSpades(self._computer._cards[i]):
							player_count += 5
						else:
							computer_count += 5

					elif self._player._cards[i].suit == "Spades" and self._computer._cards[i].suit != "Spades":
						player_count += 5

					elif self._player._cards[i].suit == "Clubs" and self._computer._cards[i].suit == "Clubs":
						if self.scoreClubs(self._player._cards[i]) > self.scoreClubs(self._computer._cards[i]):
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
							if self.scoreHearts(self._player._cards[i]) > self.scoreHearts(self._computer._cards[i]):
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
	def scoreTrumpSpades(self, input):
		score = 0
		if input.rank == 5:
			score += 14 
		elif input.rank == 11:
			score += 13
		elif input.rank == 1:
			score += 12
		elif input.rank == 13: 
			score += 11
		elif input.rank == 12:
			score += 10
		elif input.rank == 2:
			score += 9
		elif input.rank == 3:
			score += 8
		elif input.rank == 4:
			score += 7
		elif input.rank == 6:
			score += 6
		elif input.rank == 7:
			score += 5
		elif input.rank == 8:
			score += 4
		elif input.rank == 9:
			score += 3
		elif input.rank == 10:
			score += 2
		return score

	def scoreTrumpClubs(self, input):
		score = 0
		if input.rank == 5:
			score += 14 
		elif input.rank == 11:
			score += 13
		elif input.rank == 1:
			score += 12
		elif input.rank == 13: 
			score += 11
		elif input.rank == 12:
			score += 10
		elif input.rank == 2:
			score += 9
		elif input.rank == 3:
			score += 8
		elif input.rank == 4:
			score += 7
		elif input.rank == 6:
			score += 6
		elif input.rank == 7:
			score += 5
		elif input.rank == 8:
			score += 4
		elif input.rank == 9:
			score += 3
		elif input.rank == 10:
			score += 2
		return score

	def scoreTrumpDiamonds(self, input):
		score = 0
		if input.rank == 5:
			score += 14 
		elif input.rank == 11:
			score += 13
		elif input.rank == 1:
			score += 12
		elif input.rank == 13: 
			score += 11
		elif input.rank == 12:
			score += 10
		elif input.rank == 10:
			score += 9
		elif input.rank == 9:
			score += 8
		elif input.rank == 8:
			score += 7
		elif input.rank == 7:
			score += 6
		elif input.rank == 6:
			score += 5
		elif input.rank == 4:
			score += 4
		elif input.rank == 3:
			score += 3
		elif input.rank == 2:
			score += 2
		return score

	def scoreTrumpHearts(self, input):
		score = 0
		if input.rank == 5:
			score += 14 
		elif input.rank == 11:
			score += 13
		elif input.rank == 1:
			score += 12
		elif input.rank == 13: 
			score += 11
		elif input.rank == 12:
			score += 10
		elif input.rank == 10:
			score += 9
		elif input.rank == 9:
			score += 8
		elif input.rank == 8:
			score += 7
		elif input.rank == 7:
			score += 6
		elif input.rank == 6:
			score += 5
		elif input.rank == 4:
			score += 4
		elif input.rank == 3:
			score += 3
		elif input.rank == 2:
			score += 2
		return score

	def scoreSpades(self, input):
		score = 0
		if input.rank == 13:
			score += 14 
		elif input.rank == 12:
			score += 13
		elif input.rank == 11:
			score += 12
		elif input.rank == 1: 
			score += 11
		elif input.rank == 2:
			score += 10
		elif input.rank == 3:
			score += 9
		elif input.rank == 4:
			score += 8
		elif input.rank == 5:
			score += 7
		elif input.rank == 6:
			score += 6
		elif input.rank == 7:
			score += 5
		elif input.rank == 8:
			score += 4
		elif input.rank == 9:
			score += 3
		elif input.rank == 10:
			score += 2
		return score

	def scoreClubs(self, input):
		score = 0
		if input.rank == 13:
			score += 14 
		elif input.rank == 12:
			score += 13
		elif input.rank == 11:
			score += 12
		elif input.rank == 1: 
			score += 11
		elif input.rank == 2:
			score += 10
		elif input.rank == 3:
			score += 9
		elif input.rank == 4:
			score += 8
		elif input.rank == 5:
			score += 7
		elif input.rank == 6:
			score += 6
		elif input.rank == 7:
			score += 5
		elif input.rank == 8:
			score += 4
		elif input.rank == 9:
			score += 3
		elif input.rank == 10:
			score += 2
		return score

	def scoreHearts(self, input):
		score = 0
		if input.rank == 13:
			score += 14 
		elif input.rank == 12:
			score += 13
		elif input.rank == 11:
			score += 12
		elif input.rank == 10: 
			score += 11
		elif input.rank == 9:
			score += 10
		elif input.rank == 8:
			score += 9
		elif input.rank == 7:
			score += 8
		elif input.rank == 6:
			score += 7
		elif input.rank == 5:
			score += 6
		elif input.rank == 4:
			score += 5
		elif input.rank == 3:
			score += 4
		elif input.rank == 2:
			score += 3
		return score

	def scoreDiamonds(self, input):
		score = 0
		if input.rank == 13:
			score += 14 
		elif input.rank == 12:
			score += 13
		elif input.rank == 11:
			score += 12
		elif input.rank == 10: 
			score += 11
		elif input.rank == 9:
			score += 10
		elif input.rank == 8:
			score += 9
		elif input.rank == 7:
			score += 8
		elif input.rank == 6:
			score += 7
		elif input.rank == 5:
			score += 6
		elif input.rank == 4:
			score += 5
		elif input.rank == 3:
			score += 4
		elif input.rank == 2:
			score += 3
		elif input.rank == 1:
			score += 2
		return score
