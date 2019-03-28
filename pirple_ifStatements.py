# -----------------------------------------------------------------------------------
# HOMEWORK #2: IF STATEMENTS
# -----------------------------------------------------------------------------------
'''Create a function that accepts 3 parameters/numbers and checks for equality among them,
returning True if 2 or more are equal

extra: ensure that strings can be entered for comparison'''


def check_equality(a, b, c):
	'''compares the value of three numbers to each other'''

	if int(a) == int(b) or int(a) == int(c) or int(b) == int(c):
		return True
	else:
		return False


# test function
# print(check_equality(3, 3, 100))			# True
# print(check_equality(1, 4, 7))				# False
# print(check_equality(600, 8, 600))		# True
# print(check_equality(600, 8, "600"))	# True

print(check_equality(a=input('First #: '), b=input('Second #: '), c=input('Third #: ')))

