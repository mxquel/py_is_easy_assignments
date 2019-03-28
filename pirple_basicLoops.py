# -----------------------------------------------------------------------------------
# HOMEWORK #5: BASIC LOOPS
# -----------------------------------------------------------------------------------
'''For the numbers from 1 to 100

	if the number is a multiple of three print "Fizz" 
	if the number is a multiple of five print "Buzz" 
	if the number is a multiple of of both three and five print "FizzBuzz"

	In all other instances print the number
'''

def print_fizz_buzz(lower, upper):
	for i in range(lower, upper + 1):
		if i % 3 == 0 and i % 5 == 0:
			print('FizzBuzz')
		elif i % 3 == 0:
			print('Fizz')
		elif i % 5 == 0:
			print('Buzz')
		else:
			print(i)

print_fizz_buzz(1, 100)