# -----------------------------------------------------------------------------------
# PROJECT #1: SIMPLE GAME
# -----------------------------------------------------------------------------------
'''CONNECT 4
	traditional board is 7 columns x 6 rows
	21 pieces per player
	first player to 4 in a row, column or diagonally wins
	pieces build on each other from the bottom up
	alternatively game ends when all slots are filled

	1. draw initial game board
	2. ask first player (associated with x) to choose a column
	2. check if column still has open fields
	3. if so execute first move (make own function)
			a. update symbol at position in board with symbol
			b. increase row value for that particular column
	4. check if player has won with the move (make separate function)
			a. print congratulations or and end game
			c. switch players/ symbol for next turn
	4. redraw updated game board
	4. check if there are still possible moves left
			a. print consolation message and end the game
			b. turn of second player (o)

extra: try colorful pieces instead of x and o (e.g. unicode or packages such as termcolor)
'''

# board markers
s = '|'
f = '––-'
e = '   '
p = ' '

# preset for columns and rows
columns = 7
rows = 6
horizontal = columns * 2 + 1
vertical = rows * 2


#  fields variable returned from set_up board function

#  ['|   |   |   |   |   |   |   |',   # fields[0][2],
#   ' ––- ––- ––- ––- ––- ––- ––- ',
#   '|   |   |   | X |   |   |   |',   # fields[2][2],
#   ' ––- ––- ––- ––- ––- ––- ––- ',
#   '|   |   |   | X | X |   |   |',   # fields[4][2],
#   ' ––- ––- ––- ––- ––- ––- ––- ',
#   '|   |   |   | X | O |   |   |',   # fields[6][2],
#   ' ––- ––- ––- ––- ––- ––- ––- ',
#   '|   |   | X | X | O |   |   |',   # fields[8][2], fields[8][6], fields[8][10], ..., fields[8][26]
#   ' ––- ––- ––- ––- ––- ––- ––- ',
#   '|   | X | O | O | O | O |   |',  # fields[10][2], fields[10][6], fields[10][10], ..., fields[10][26]
#   ' ––- ––- ––- ––- ––- ––- ––- ']


# vertical and horizontal indices
# v_is = list(range(0, 12, 2)) # [0, 2, 4, 6, 8, 10]
# h_is = list(range(2, 29, 4)) # [2, 6, 10, 14, 18, 22, 26]

# board map in indices
# list(zip(sorted(v_is * 7), h_is * 6))

# [(0, 2), (0, 6), (0, 10), (0, 14), (0, 18), (0, 22), (0, 26),
# (2, 2), (2, 6), (2, 10), (2, 14), (2, 18), (2, 22), (2, 26),
# (4, 2), (4, 6), (4, 10), (4, 14), (4, 18), (4, 22), (4, 26),
# (6, 2), (6, 6), (6, 10), (6, 14), (6, 18), (6, 22), (6, 26),
# (8, 2), (8, 6), (8, 10), (8, 14), (8, 18), (8, 22), (8, 26),
# (10, 2), (10, 6), (10, 10), (10, 14), (10, 18), (10, 22), (10, 26)]


# transposed mapp:
# list(zip(v_is * 9, sorted(h_is * 6)))

# [(0, 2), (2, 2), (4, 2), (6, 2), (8, 2), (10, 2),
# (0, 6), (2, 6), (4, 6), (6, 6), (8, 6), (10, 6),
# (0, 10), (2, 10), (4, 10), (6, 10), (8, 10), (10, 10),
# (0, 14), (2, 14), (4, 14), (6, 14), (8, 14), (10, 14),
# (0, 18), (2, 18), (4, 18), (6, 18), (8, 18), (10, 18),
# (0, 22), (2, 22), (4, 22), (6, 22), (8, 22), (10, 22),
# (0, 26), (2, 26), (4, 26), (6, 26), (8, 26), (10, 26)]


right_leaning = [
	[(0, 22), (2, 18), (4, 14), (6, 10), (8, 6), (10, 2)],
	[(0, 26), (2, 22), (4, 18), (6, 14), (8, 10), (10, 6)],
	[(2, 26), (4, 22), (6, 18), (8, 14), (10, 10)],
	[(4, 26), (6, 22), (8, 18), (10, 14)],
	[(0, 18), (2, 14), (4, 10), (6, 6), (8, 2)],
	[(0, 14), (2, 10), (4, 6), (6, 2)]]


left_leaning = [
 [(0, 6), (2, 10), (4, 14), (6, 18), (8, 22), (10, 26)],
	[(0, 2), (2, 6), (4, 10), (6, 14), (8, 18), (10, 22)],
	[(2, 2), (4, 6), (6, 10), (8, 14), (10, 18)],
	[(4, 2), (6, 6), (8, 10), (10, 14)],
	[(0, 10), (2, 14), (4, 18), (6, 22), (8, 26)],
	[(0, 14), (2, 18), (4, 22), (6, 26)]]


diagonal_slices = [(0, 6), (6, 12), (12, 17), (17, 21), (21, 26), (26, 30)]



def setup_board(h=15, v=12):
  row = ''.join([(s if c % 2 == 0 else e) for c in range(h)])
  devider = ''.join([(p if c % 2 == 0 else f) for c in range(h)])
  fields = [(row if place % 2 == 0 else devider) for place in range(v)]

  return fields


def print_board(board):
  print('\n'.join(board))

  return True


def test_horizontal(board):
	t = [c for c in board if 'X | X | X | X' in c or 'O | O | O | O' in c]
	if t:
		return True
	else:
		return False


def test_vertical(board):
	a = list(range(0, 12, 2)) * 9
	b = sorted(list(range(2, 29, 4)) * 6)
	c = list(zip(a, b))

	n = [board[i][y] for i, y in c]
	m = [''.join(n[t:t+6]) for t in range(0, 42, 6)]
	# ['      ', '    XX', '    XO', ' XXXXO', '  XOOO', '     O', '      ']

	if [i for i in m if 'XXXX' in i]:
		return True
	else:
		return False


def test_diagonal(board, diagonal_type):
	k = [board[x][y] for diagonal in diagonal_type for x, y in diagonal]
	l = [''.join(k[i:y]) for i, y in diagonal_slices]

	if [x for x in l if 'XXXX' in x or 'OOOO' in x]:
		return True
	else:
		return False



def check_winner():
	pass



def make_move():
	pass



test_board = [
 '|   |   |   |   |   |   |   |',
 ' ––- ––- ––- ––- ––- ––- ––- ',
 '|   |   |   | X |   |   |   |',
 ' ––- ––- ––- ––- ––- ––- ––- ',
 '|   |   |   | X | X |   |   |',
 ' ––- ––- ––- ––- ––- ––- ––- ', 
 '|   |   |   | X | O |   |   |',
 ' ––- ––- ––- ––- ––- ––- ––- ',
 '|   |   | X | X | O |   |   |',
 ' ––- ––- ––- ––- ––- ––- ––- ',
 '|   | X | O | O | O | O |   |',
 ' ––- ––- ––- ––- ––- ––- ––- ']

test_board_2 = [
 '|   |   |   |   |   |   |   |',
 ' ––- ––- ––- ––- ––- ––- ––- ',
 '|   |   |   | X |   |   |   |',
 ' ––- ––- ––- ––- ––- ––- ––- ',
 '|   |   |   | B | X |   |   |',
 ' ––- ––- ––- ––- ––- ––- ––- ',
 '|   |   |   | X | O |   |   |',
 ' ––- ––- ––- ––- ––- ––- ––- ',
 '|   |   | X | X | O |   |   |',
 ' ––- ––- ––- ––- ––- ––- ––- ',
 '|   | X | O | A | O | O |   |',
 ' ––- ––- ––- ––- ––- ––- ––- ']


test_board_3 = [
 '|   |   |   | F | E | A | B |',
 ' ––- ––- ––- ––- ––- ––- ––- ',
 '|   |   | F | E | X | B | C |',
 ' ––- ––- ––- ––- ––- ––- ––- ',
 '|   | F | E | X | O | C | D |',
 ' ––- ––- ––- ––- ––- ––- ––- ',
 '| F | E | O | O | C | D |   |',
 ' ––- ––- ––- ––- ––- ––- ––- ',
 '| E | O | O | C | D |   |   |',
 ' ––- ––- ––- ––- ––- ––- ––- ',
 '| A | O | C | D |   |   |   |',
 ' ––- ––- ––- ––- ––- ––- ––- ']



test_board_4 = [
 '| B | A | E | F |   |   |   |',
 ' ––- ––- ––- ––- ––- ––- ––- ',
 '| C | B | A | E | F |   |   |',
 ' ––- ––- ––- ––- ––- ––- ––- ',
 '| X | O | B | A | E | F |   |',
 ' ––- ––- ––- ––- ––- ––- ––- ',
 '|   | X | O | B | A | E | F |',
 ' ––- ––- ––- ––- ––- ––- ––- ',
 '|   |   | O | O | B | A | E |',
 ' ––- ––- ––- ––- ––- ––- ––- ',
 '|   |   |   | O | O | B | A |',
 ' ––- ––- ––- ––- ––- ––- ––- ']







# game_board = setup_board()
# print_board(game_board)
