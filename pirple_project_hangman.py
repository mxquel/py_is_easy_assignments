
# -----------------------------------------------------------------------------------
# PROJECT #2: HANGMAN
# -----------------------------------------------------------------------------------
'''
	1. ask player 1 for a word with at least 3 letters
	2. print underscores representing the letters in the word (hidden word)
	3. ask second player for his guess and check that it is a lower case letter
	4. check off letter and check if it is in the word
		a. if yes reveal letter in word, check if won and ask for another letter if not
		b. if not reprint hidden word, decrease attempts (max. 8) and ask for another letter
	5. repeat until player 1 wins or there are no more attempts left
	6. print out congratulations to whichever player won

extra: single player mode = select a random word for the round
'''

from string import ascii_lowercase
from random import randint


words = ['unnatural', 'afford', 'program', 'black', 'rhyme', 'zipper', 'porter', 'idiotic',
'wooden', 'quirky', 'flood', 'supply', 'machine', 'return', 'cute', 'quince', 'jolly', 'peel',
'adjoining', 'flesh', 'mouth', 'suppose', 'arrest', 'hope']

attempts = 7
remaining_letters = list(ascii_lowercase)


def select_word():
	return words[randint(0, len(words) - 2)]


def print_field(field):
	print(' '.join(field))


def make_guess():
	while True:
		guess = input('Please enter your guess: ')

		if len(guess) != 1:
			print('You must guess a single letter.')
		elif guess.isnumeric():
			print('That is not a letter.')
		else:
			if guess not in remaining_letters:
				print('You have already guessed that letter.')
			else:
				remaining_letters.remove(guess)
				return guess


# ----------------------------- game play -----------------------------

mode = input('Please enter 1 for single or 2 for two player mode: ')

if mode.strip() == '1':
	player_two = 'The computer'
	word = select_word()
elif mode.strip() == '2':
	player_two = input('Please enter the name of the player that provides the word: ')
	word = (input('Please enter your word: ')).lower()

player_one = input('Please enter the name of the guessing player: ')

print('\n' * 30)

field = ['_' for letter in list(word)]

while attempts > 0 and '_' in field:
	print_field(field)
	print('Unguessed letters:', ' '.join(remaining_letters))
	print('Remaining attempts:', attempts)
	turn = make_guess()

	if turn in list(word):
		positions = [i for i, letter in enumerate(list(word)) if letter == turn]

		for position in positions:
			field[position] = turn
	else:
		print(turn, 'is not in the word.')
		attempts -= 1


print_field(field)

if '_' not in field:
	print(f'Congratulations! {player_one} has won.')
else:
	print(f'Congratulations! {player_two} has won.')
