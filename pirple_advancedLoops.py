# -----------------------------------------------------------------------------------
# HOMEWORK #6: ADVANCED LOOPS
# -----------------------------------------------------------------------------------
'''Create a function that draws a playing board. The number of rows and columns are the same. 
After drawing the board, your function should return True.

extra: determine the maximum width and height that your terminal and screen can comfortably fit 
without wrapping. If someone passes a value greater than the maximum, the function should return False
'''

# markers
s = '|'
f = '––'
e = '  '
p = ' '


def setup_board(matrix=3):
  # determine necessary character spaces for a specific matrix
  places = matrix + (matrix - 1)

  row = ''.join([(e if c % 2 == 0 else s) for c in range(places)])
  devider = ''.join([(f if c % 2 == 0 else p) for c in range(places)])
  fields = [(row if place % 2 == 0 else devider) for place in range(places)]

  return places, fields


def print_board(board):
  places, fields = board
  
  print('\n'.join(fields))
  
  return True


print_board(setup_board())
