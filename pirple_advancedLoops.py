# -----------------------------------------------------------------------------------
# HOMEWORK #6: ADVANCED LOOPS
# -----------------------------------------------------------------------------------
'''Create a function that draws a playing board. The number of rows and columns are the same. 
After drawing the board, your function should return True.
'''

# markers
s = '|'
f = '––'
e = '  '
p = ' '


def setup_board(matrix=3):
  # deterimine necessary character spaces for a specific matrix
  places = matrix + (matrix - 1)

  row = ''.join([(e if c % 2 == 0 else s) for c in range(places)])
  devider = ''.join([(f if c % 2 == 0 else p) for c in range(places)])
  board = '\n'.join([(row if place % 2 == 0 else devider) for place in range(places)])

  print(board)

  return True


setup_board()
