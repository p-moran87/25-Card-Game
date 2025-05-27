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
		
	def getCards(self):
		return self._cards

class Computer(Player):
	def __init__(self, cards):
		""" Conceal the computer's hand of cards"""
		Player.__init__(self, cards)

		#for card in self._cards:
		#	card.turn()

class Trumps(Player):
	def __init__(self, cards):
		"""show card"""
		Player.__init__(self, cards)

class CardGame(object):
	def __init__(self):
		self._deck = Deck()
		self._deck.shuffle()
		
		# Pass the player and the computer 3 cards each, follwed by 2 cards each
		player_deal1 = [self._deck.deal(), self._deck.deal(), self._deck.deal()]
		computer_deal1 = [self._deck.deal(), self._deck.deal(), self._deck.deal()]

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
		"""Returns a the trump card."""
		return self._trumps.getCards()

	def RobCard(self,num_dealt_cards):
		""" checks to see who has the rob"""
		if (self._trumps._cards[0].rank == 1):
			if num_dealt_cards == 5:
				return "Turned an Ace - you can rob!"
			else:
				return "Computer turned Ace - it can rob!"

		for i in range(5):
			if self._player._cards[i].rank == 1  and self._trumps._cards[0].suit == self._player._cards[i].suit:
				return "Congrats, you have the rob!"
			elif self._computer._cards[i].rank == 1 and self._trumps._cards[0].suit == self._computer._cards[i].suit:
				return "The computer has the rob!"

	def getDealer(self,num_dealt_cars):
		if num_dealt_cars == 5:
			dealer = "player"
		else:
			dealer = "computer"
		return dealer

	def getPoints(self,p1_card, comp_card):
		"""Returns the points scored by player for new round"""
		player_count = 0
		computer_count = 0

		if self._trumps._cards[0].suit == "Spades":
			if p1_card.suit == "Spades" and comp_card.suit == "Spades":
				if val_list_trump_spades.index(p1_card.rank) > val_list_trump_spades.index(comp_card.rank):
					player_count += 5
				else:
					computer_count += 5

			elif p1_card.suit == "Spades" and comp_card.suit != "Spades":
				if (p1_card.rank != 5 or p1_card.rank != 11) and (comp_card.suit == "Hearts" and comp_card.rank == 1):
					computer_count += 5
				else:
					player_count += 5
			elif p1_card.suit != "Spades" and comp_card.suit == "Spades":
				if (p1_card.suit == "Hearts" and p1_card.rank == 1) and (comp_card.rank != 5 or comp_card.rank != 11):
					player_count += 5
				else:
					computer_count += 5

			elif p1_card.suit != "Spades" and comp_card.suit != "Spades":
				if p1_card.suit == "Clubs" and comp_card.suit == "Clubs":
					if val_list_clubs.index(p1_card.rank) > val_list_clubs.index(comp_card.rank):
						player_count += 5
					else:
						computer_count += 5
				elif p1_card.suit == "Clubs" and comp_card.suit != "Clubs":
					player_count += 5

				elif p1_card.suit == "Hearts" and comp_card.suit == "Hearts":
					if p1_card.suit == "Hearts" and p1_card.rank == 1:
						player_count += 5
					elif comp_card.suit == "Hearts" and comp_card.rank == 1:
						computer_count += 5
					else:
						if val_list_hearts.index(p1_card.rank) > val_list_hearts.index(comp_card.rank):
							player_count += 5
						else:
							computer_count += 5
				elif p1_card.suit == "Hearts" and comp_card.suit != "Hearts":
					player_count += 5

				elif p1_card.suit == "Diamonds" and comp_card.suit == "Diamonds":
					if val_list_diamonds.index(p1_card.rank) > val_list_diamonds.index(comp_card.rank):
						player_count += 5
					else:
						computer_count += 5
				elif p1_card.suit == "Diamonds" and comp_card.suit != "Diamonds":
					player_count += 5

		elif self._trumps._cards[0].suit == "Clubs":
			if p1_card.suit == "Clubs" and comp_card.suit == "Clubs":
				if val_list_trump_clubs.index(p1_card.rank) > val_list_trump_clubs.index(comp_card.rank):
					player_count += 5
				else:
					computer_count += 5

			elif p1_card.suit == "Clubs" and comp_card.suit != "Clubs":
				if (p1_card.rank != 5 or p1_card.rank != 11) and (comp_card.suit == "Hearts" and comp_card.rank == 1):
					computer_count += 5
				else:
					player_count += 5
			elif p1_card.suit != "Clubs" and comp_card.suit == "Clubs":
				if (p1_card.suit == "Hearts" and p1_card.rank == 1) and (comp_card.rank != 5 or comp_card.rank != 11):
					player_count += 5
				else:
					computer_count += 5

			elif p1_card.suit != "Clubs" and comp_card.suit != "Clubs":
				if p1_card.suit == "Spades" and comp_card.suit == "Spades":
					if val_list_spades.index(p1_card.rank) > val_list_spades.index(comp_card.rank):
						player_count += 5
					else:
						computer_count += 5
				elif p1_card.suit == "Spades" and comp_card.suit != "Spades":
					player_count += 5

				elif p1_card.suit == "Hearts" and comp_card.suit == "Hearts":
					if p1_card.suit == "Hearts" and p1_card.rank == 1:
						player_count += 5
					elif comp_card.suit == "Hearts" and comp_card.rank == 1:
						computer_count += 5
					else:
						if val_list_hearts.index(p1_card.rank) > val_list_hearts.index(comp_card.rank):
							player_count += 5
						else:
							computer_count += 5
				elif p1_card.suit == "Hearts" and comp_card.suit != "Hearts":
					player_count += 5

				elif p1_card.suit == "Diamonds" and comp_card.suit == "Diamonds":
					if val_list_diamonds.index(p1_card.rank) > val_list_diamonds.index(comp_card.rank):
						player_count += 5
					else:
						computer_count += 5
				elif p1_card.suit == "Diamonds" and comp_card.suit != "Diamonds":
					player_count += 5

		elif self._trumps._cards[0].suit == "Hearts":
			if p1_card.suit == "Hearts" and comp_card.suit == "Hearts":
				if val_list_trump_hearts.index(p1_card.rank) > val_list_trump_hearts.index(comp_card.rank):
					player_count += 5
				else:
					computer_count += 5
			elif p1_card.suit == "Hearts" and comp_card.suit != "Hearts":
				player_count += 5

			elif p1_card.suit != "Hearts" and comp_card.suit == "Hearts":
				computer_count += 5

			elif p1_card.suit != "Hearts" and comp_card.suit != "Hearts":
				if p1_card.suit == "Spades" and comp_card.suit == "Spades":
					if val_list_spades.index(p1_card.rank) > val_list_spades.index(comp_card.rank):
						player_count += 5
					else:
						computer_count += 5
				elif p1_card.suit == "Spades" and comp_card.suit != "Spades":
					player_count += 5

				if p1_card.suit == "Clubs" and comp_card.suit == "Clubs":
					if val_list_clubs.index(p1_card.rank) > val_list_clubs.index(comp_card.rank):
						player_count += 5
					else:
						computer_count += 5

				elif p1_card.suit == "Clubs" and comp_card.suit != "Clubs":
					player_count += 5

				if p1_card.suit == "Diamonds" and comp_card.suit == "Diamonds":
					if val_list_diamonds.index(p1_card.rank) > val_list_diamonds.index(comp_card.rank):
						player_count += 5
					else:
						computer_count += 5
				elif p1_card.suit == "Diamonds" and comp_card.suit != "Diamonds":
					player_count += 5

		elif self._trumps._cards[0].suit == "Diamonds":
			if p1_card.suit == "Diamonds" and comp_card.suit == "Diamonds":
				if val_list_trump_diamonds.index(p1_card.rank) > val_list_trump_diamonds.index(comp_card.rank):
					player_count += 5
				else:
					computer_count += 5

			elif p1_card.suit == "Diamonds" and comp_card.suit != "Diamonds":
				if (p1_card.rank != 5 or p1_card.rank != 11) and (comp_card.suit == "Hearts" and comp_card.rank == 1):
					computer_count += 5
				else:
					player_count += 5
			elif p1_card.suit != "Diamonds" and comp_card.suit == "Diamonds":
				if (p1_card.suit == "Hearts" and p1_card.rank == 1) and (comp_card.rank != 5 or comp_card.rank != 11):
					player_count += 5
				else:
					computer_count += 5

			elif p1_card.suit != "Diamonds" and comp_card.suit != "Diamonds":
				if p1_card.suit == "Spades" and comp_card.suit == "Spades":
					if val_list_spades.index(p1_card.rank) > val_list_spades.index(comp_card.rank):
						player_count += 5
					else:
						computer_count += 5

				elif p1_card.suit == "Spades" and comp_card.suit != "Spades":
					player_count += 5

				elif p1_card.suit == "Clubs" and comp_card.suit == "Clubs":
					if val_list_clubs.index(p1_card.rank) > val_list_clubs.index(comp_card.rank):
						player_count += 5
					else:
						computer_count += 5

				elif p1_card.suit == "Clubs" and comp_card.suit != "Clubs":
					player_count += 5

				elif p1_card.suit == "Hearts" and comp_card.suit == "Hearts":
					if p1_card.suit == "Hearts" and p1_card.rank == 1:
						player_count += 5
					elif comp_card.suit == "Hearts" and comp_card.rank == 1:
						computer_count += 5
					else:
						if val_list_hearts.index(p1_card.rank) > val_list_hearts.index(comp_card.rank):
							player_count += 5
						else:
							computer_count += 5
				elif p1_card.suit == "Hearts" and comp_card.suit != "Hearts":
					player_count += 5

		return player_count, computer_count

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
val_list_trump_spades = list(Rank_Trump_Spades.values())
val_list_trump_clubs = list(Rank_Trump_Clubs.values())
val_list_trump_hearts = list(Rank_Trump_Hearts.values())
val_list_trump_diamonds = list(Rank_Trump_Diamonds.values())

val_list_spades = list(Rank_Spades.values())
val_list_clubs = list(Rank_Clubs.values())
val_list_hearts = list(Rank_Hearts.values())
val_list_diamonds = list(Rank_Diamonds.values())
