# -----------------------------------------------------------------------------------
# PROJECT #3: PICK A CARD GAME! GO FISH
# -----------------------------------------------------------------------------------
'''Game play:
ask for player names at the beginning
if 2 or 3 players start off by drawing 5 otherwise 7 cards, each at random
take turns in asking for cards of rank that is in their hand and either
	a. draw from the pile if the other player does not have the card
	b. or recieve the card(s) and ask again
make players take turns after each unsuccessful request or draw
put down each completed book/ set on the table
game is over when all thirteen books are won
the winner is the player with the highest score, i.e. most books

if player runs out of cards let them draw from the ocean/ pile before taking a turn

https://en.wikipedia.org/wiki/Go_Fish
'''

from random import shuffle

class Ocean():
	"""
	deck of cards where suits are not important only that there is four of each rank.
	use shuffel_deck function to randomly sort cards in the deck
	"""
	def __init__(self):
		self.deck = list('234567890JQKA' * 4)
		self.remaining_cards = len(self.deck)


	def shuffle_deck(self):
		shuffle(self.deck)


	def pop(self):
		return self.deck.pop()


class Player():
	"""
	initialise player with a unique name and empty attributes for hand, books and score
	provides a method to go_fish, hand_over_cards, pocket_cards, check_for_books
	"""
	def __init__(self, name):
		self.name = name.title()
		self.hand = []
		self.books = []
		self.score = len(self.books)


	def go_fish(self, ocean):
		self.hand.append(ocean.pop())


	def hand_over_cards(self, card):
		fished = []
		while card in self.hand:
			self.hand.remove(card)
			fished.append(card)

		return fished


	def pocket_cards(self, cards):
		self.hand.extend(cards)


	def check_for_books(self):
		for card in self.hand:
			if self.hand.count(card) == 4:
				for _ in range(4):
					self.hand.remove(card)

				self.books.append(card)
				self.score += 1
				print('{} fished all {}\s.'.format(self.name, card))



class Game():
	"""
	defines initial varialbes for a game and contains methods to deal_cards, find_index_by_name
	for each player, reduce the number of fishes in the ocean (cull_ocean) and sum_scores
	"""
	def __init__(self, participants):
		self.ocean = Ocean()
		self.ocean.shuffle_deck()
		self.fish_left = self.ocean.remaining_cards
		self.players = {i: Player(participant) for i, participant in enumerate(participants)}
		self.number_of_players = len(self.players)


	def deal_cards(self):
		if self.number_of_players > 4:
			initial_hand = 5
		else:
			initial_hand = 7

		[self.players[index].hand.append(self.ocean.deck.pop()) for _ in range(initial_hand) for index in self.players]
		self.fish_left -= initial_hand * self.number_of_players

		# check whether anyone has already got a book
		[self.players[index].check_for_books() for index in self.players]


	def find_index_by_name(self, name):
		for index in self.players:
			if self.players[index].name == name:
				return index


	def cull_ocean(self):
		self.fish_left -= 1


	def is_fish_in_ocean(self):
		return self.fish_left != 0


	def sum_scores(self):
		scores = [self.players[index].score for index in self.players]
		return scores, sum(scores)



# ----------------------------------------- game setup ----------------------------------------

participants = []

while not len(participants) >= 2:
	participants = input('Please enter the names of all players separted by a space: ').split()

play = Game(participants)
play.deal_cards()


# ----------------------------------------- game play -----------------------------------------

turn = 0

while True:
	current_player = play.players[turn]

	# if current player has no cards left make them draw from the open pile
	while not current_player.hand:
		if play.is_fish_in_ocean():
			current_player.go_fish(play.ocean)
			play.cull_ocean()
		else:
			if turn < play.number_of_players - 1:
				turn += 1
			else:
				turn = 0

			current_player = play.players[turn]

	print(f'\n\n{current_player.name} it is your turn.\nYour current hand is: {" ".join(sorted(current_player.hand))}')

	try:
		player_choice = (input('Please choose a player to ask for a card: ')).title().strip()
		card_choice = (input('Please choose a card: ')).upper().strip()
		ask = play.find_index_by_name(player_choice)

		if card_choice in current_player.hand:
			if card_choice in play.players[ask].hand:
				current_player.pocket_cards(play.players[ask].hand_over_cards(card_choice))
				current_player.check_for_books()
			else:
				if play.is_fish_in_ocean():
					print('Go Fish!')
					current_player.go_fish(play.ocean)
					play.cull_ocean()

					if current_player.hand.count(current_player.hand[-1]) > 1:
						print('Your fishing expeditions was lucky.')
						current_player.check_for_books()
					else:
						if turn < play.number_of_players - 1:
							turn += 1
						else:
							turn = 0
				else:
					print('There are no more fish in the sea.')
					if turn < play.number_of_players - 1:
						turn += 1
					else:
						turn = 0
		else:
			print('Please choose a card that is already in your hand.')

		if play.sum_scores()[1] == 13:
			winners = [i for i, score in enumerate(play.sum_scores()[0]) if score == max(play.sum_scores()[0])]
			congrats = '{} won the game with {} points'
			print('\n', '_' * 23, 'GAME OVER', '_' * 23, '\n')
			[print(congrats.format(play.players[winner].name, play.players[winner].score)) for winner in winners]

			break


	except KeyError:
		print('Please choose a name of a player who is in the game.')
