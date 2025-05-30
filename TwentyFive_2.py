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

	def getPoints(self, p1_card, comp_card, led_by):
		"""Evaluate points for a trick based on rules of 25"""

		trump_suit = self._trumps._cards[0].suit

		# Define suit to ranking mappings
		trump_rankings = {
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

		suit_rankings = {
			"Spades": {13: 13, 12: 12, 11: 11, 1: 10, 2: 9, 3: 8, 4: 7, 5: 6, 6: 5, 7: 4, 8: 3, 9: 2, 10: 1},
			"Clubs": {13: 13, 12: 12, 11: 11, 1: 10, 2: 9, 3: 8, 4: 7, 5: 6, 6: 5, 7: 4, 8: 3, 9: 2, 10: 1},

			"Hearts": {1: 13, 13: 12, 12: 11, 10: 10, 9: 9, 8: 8, 7: 7, 6: 6, 5: 5, 4: 4, 3: 3, 2: 2},
			"Diamonds": {13: 13, 12: 12, 11: 11, 10: 10, 9: 9, 8: 8, 7: 7, 6: 6, 5: 5, 4: 4, 3: 3, 2: 2, 1: 1}
			}

		def get_card_value(card):
			"""Get card rank based on whether it's trump"""
			if card.suit == trump_suit:
				return trump_rankings[trump_suit][card.rank]
			else:
				return suit_rankings[card.suit][card.rank]

	    # Decide led suit
		led_card = p1_card if led_by == "player" else comp_card
		response_card = comp_card if led_by == "player" else p1_card

		# Special case: Ace of Hearts is ALWAYS the 3rd highest trump
		if p1_card.suit == "Hearts" and p1_card.rank == 1:
			if comp_card.suit == trump_suit and (comp_card.rank == 5 or comp_card.rank == 11):
				return (0, 5)
			else:
				return (5, 0)

	    # Case 1: Both play same suit
		if p1_card.suit == comp_card.suit:
			if get_card_value(p1_card) > get_card_value(comp_card):
				return (5, 0)
			else:
				return (0, 5)

		# Case 2: Trump beats non-trump
		if p1_card.suit == trump_suit and comp_card.suit != trump_suit:
			return (5, 0)
		elif comp_card.suit == trump_suit and p1_card.suit != trump_suit:
			return (0, 5)

		# Case 3: Neither card is trump
		if p1_card.suit == led_card.suit:
			return (5, 0)
		elif comp_card.suit == led_card.suit:
			return (0, 5)
	    
		# Edge case: No one followed led suit (should not happen in valid play)
		# Default to whoever played the higher value card in this case
		if get_card_value(p1_card) > get_card_value(comp_card):
			return (5, 0)
		else:
			return (0, 5)