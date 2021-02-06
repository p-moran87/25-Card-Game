#for card in self._cards:
		for i in range(0,5):
			if self._trumps._cards[0].suit == "Spades":
				if self._player._cards[i].suit == "Spades" and self._computer._cards[i].suit == "Spades":
					if self.scoreTrumpSpades(self._player._cards[i]) > self.scoreTrumpSpades(self._computer._cards[i]):
						player_count += 5
					else:
						computer_count += 5

				elif self._player._cards[i].suit == "Spades" and self._computer._cards[i].suit != "Spades":
					player_count += 5

				elif self._player._cards[i].suit != "Spades" and self._computer._cards[i].suit == "Spades":
					computer_count += 5

				elif self._player._cards[i].suit != "Spades" and self._computer._cards[i].suit != "Spades":

					if self._player._cards[i].suit == "Clubs" and self._computer._cards[i].suit == "Clubs":

						if self.scoreClubs(self._player._cards[i]) > self.scoreClubs(self._computer._cards[i]):
							player_count += 5

						else:
							computer_count += 5

					elif self._player._cards[i].suit == "Clubs" and self._computer._cards[i].suit != "Clubs":
						player_count += 5

					if self._player._cards[i].suit == "Hearts" and self._computer._cards[i].suit == "Hearts":

						if self.scoreHearts(self._player._cards[i]) > self.scoreHearts(self._computer._cards[i]):
							player_count += 5

						else:
							computer_count += 5

					elif self._player._cards[i].suit == "Hearts" and self._computer._cards[i].suit != "Hearts":
						player_count += 5

					if self._player._cards[i].suit == "Diamonds" and self._computer._cards[i].suit == "Diamonds":

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
					player_count += 5

				elif self._player._cards[i].suit != "Clubs" and self._computer._cards[i].suit == "Clubs":
					computer_count += 5

				elif self._player._cards[i].suit != "Clubs" and self._computer._cards[i].suit != "Clubs":

					if self._player._cards[i].suit == "Spades" and self._computer._cards[i].suit == "Spades":

						if self.scoreSpades(self._player._cards[i]) > self.scoreSpades(self._computer._cards[i]):
							player_count += 5

						else:
							computer_count += 5

					elif self._player._cards[i].suit == "Spades" and self._computer._cards[i].suit != "Spades":
						player_count += 5

					if self._player._cards[i].suit == "Hearts" and self._computer._cards[i].suit == "Hearts":

						if self.scoreHearts(self._player._cards[i]) > self.scoreHearts(self._computer._cards[i]):
							player_count += 5

						else:
							computer_count += 5

					elif self._player._cards[i].suit == "Hearts" and self._computer._cards[i].suit != "Hearts":
						player_count += 5

					if self._player._cards[i].suit == "Diamonds" and self._computer._cards[i].suit == "Diamonds":

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
					player_count += 5

				elif self._player._cards[i].suit != "Diamonds" and self._computer._cards[i].suit == "Diamonds":
					computer_count += 5

				elif self._player._cards[i].suit != "Diamonds" and self._computer._cards[i].suit != "Diamonds":

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

					if self._player._cards[i].suit == "Hearts" and self._computer._cards[i].suit == "Hearts":

						if self.scoreHearts(self._player._cards[i]) > self.scoreHearts(self._computer._cards[i]):
							player_count += 5

						else:
							computer_count += 5
					elif self._player._cards[i].suit == "Hearts" and self._computer._cards[i].suit != "Hearts":
						player_count += 5

		return player_count, computer_count

	""" Defines the rules and rankings of cards """
	def scoreTrumpSpades(self, input):
		score = 0
		if input.rank == 5:
			score = 14
		elif input.rank == 11:
			score = 13
		elif input.rank == 1:
			score = 12
		elif input.rank == 13:
			score = 11
		elif input.rank == 12:
			score = 10
		elif input.rank == 2:
			score = 9
		elif input.rank == 3:
			score = 8
		elif input.rank == 4:
			score = 7
		elif input.rank == 5:
		 	score = 6
		elif input.rank == 6:
			score = 5
		elif input.rank == 7:
			score = 3
		elif input.rank == 8:
			score = 2
		elif input.rank == 9:
			score = 1
		elif input.rank == 10:
			score = 0
		return score

	def scoreTrumpClubs(self, input):
		score = 0
		if input.rank == 5:
			score = 14
		elif input.rank == 11:
			score = 13
		elif input.rank == 1:
			score = 12
		elif input.rank == 13:
			score = 11
		elif input.rank == 12:
			score = 10
		elif input.rank == 2:
			score = 9
		elif input.rank == 3:
			score = 8
		elif input.rank == 4:
			score = 7
		elif input.rank == 5:
		 	score = 6
		elif input.rank == 6:
			score = 5
		elif input.rank == 7:
			score = 3
		elif input.rank == 8:
			score = 2
		elif input.rank == 9:
			score = 1
		elif input.rank == 10:
			score = 0
		return score

	def scoreTrumpDiamonds(self, input):
		score = 0
		if input.rank == 5:
			score = 14
		elif input.rank == 11:
			score = 13
		elif input.rank == 1:
			score = 11
		elif input.rank == 13:
			score = 10
		elif input.rank == 12:
			score = 9
		elif input.rank == 10:
			score = 8
		elif input.rank == 9:
			score = 7
		elif input.rank == 8:
			score = 6
		elif input.rank == 7:
			score = 5
		elif input.rank == 6:
		 	score = 4
		elif input.rank == 5:
			score = 3
		elif input.rank == 4:
			score = 2
		elif input.rank == 3:
			score = 1
		elif input.rank == 2:
			score = 0
		return score

	def scoreTrumpHearts(self, input):
		score = 0
		if input.rank == 5:
			score = 14
		elif input.rank == 11:
			score = 13
		elif input.rank == 1:
			score = 11
		elif input.rank == 13:
			score = 10
		elif input.rank == 12:
			score = 9
		elif input.rank == 10:
			score = 8
		elif input.rank == 9:
			score = 7
		elif input.rank == 8:
			score = 6
		elif input.rank == 7:
			score = 5
		elif input.rank == 6:
		 	score = 4
		elif input.rank == 5:
			score = 3
		elif input.rank == 4:
			score = 2
		elif input.rank == 3:
			score = 1
		elif input.rank == 2:
			score = 0
		return score

	def scoreSpades(self, input):
		score = 0
		if input.rank == 13:
			score = 14
		elif input.rank == 12:
			score = 13
		elif input.rank == 11:
			score= 12
		elif input.rank == 1:
			score = 11
		elif input.rank == 2:
			score = 10
		elif input.rank == 3:
			score = 9
		elif input.rank == 4:
			score = 8
		elif input.rank == 5:
			score = 7
		elif input.rank == 6:
			score = 6
		elif input.rank == 7:
		 	score = 5
		elif input.rank == 8:
			score = 4
		elif input.rank == 9:
			score = 3
		elif input.rank == 10:
			score = 2
		return score

	def scoreClubs(self, input):
		score = 0
		if input.rank == 13:
			score = 14
		elif input.rank == 12:
			score = 13
		elif input.rank == 11:
			score= 12
		elif input.rank == 1:
			score = 11
		elif input.rank == 2:
			score = 10
		elif input.rank == 3:
			score = 9
		elif input.rank == 4:
			score = 8
		elif input.rank == 5:
			score = 7
		elif input.rank == 6:
			score = 6
		elif input.rank == 7:
		 	score = 5
		elif input.rank == 8:
			score = 4
		elif input.rank == 9:
			score = 3
		elif input.rank == 10:
			score = 2
		return score

	def scoreHearts(self, input):
		score = 0
		if input.rank == 13:
			score = 14
		elif input.rank == 12:
			score = 13
		elif input.rank == 11:
			score= 12
		elif input.rank == 10:
			score = 11
		elif input.rank == 9:
			score = 10
		elif input.rank == 8:
			score = 9
		elif input.rank == 7:
			score = 8
		elif input.rank == 6:
			score = 7
		elif input.rank == 5:
			score = 6
		elif input.rank == 4:
			score = 5
		elif input.rank == 3:
		 	score = 4
		elif input.rank == 2:
			score = 3
		return score

	def scoreDiamonds(self, input):
		score = 0
		if input.rank == 13:
			score = 14
		elif input.rank == 12:
			score = 13
		elif input.rank == 11:
			score= 12
		elif input.rank == 10:
			score = 11
		elif input.rank == 9:
			score = 10
		elif input.rank == 8:
			score = 9
		elif input.rank == 7:
			score = 8
		elif input.rank == 6:
			score = 7
		elif input.rank == 5:
			score = 6
		elif input.rank == 4:
			score = 5
		elif input.rank == 3:
		 	score = 4
		elif input.rank == 2:
			score = 3
		elif input.rank == 1:
			score = 2
		return score



