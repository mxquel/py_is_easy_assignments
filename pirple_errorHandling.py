# -----------------------------------------------------------------------------------
# HOMEWORK #11: ERROR HANDLING
# -----------------------------------------------------------------------------------
'''Choose any of the homeworks or projects you've done so far. Pick a function that
you know is particularly problematic and add try/except/finally cases to it
so that it can handle the errors more gracefully.

extra: Below your function, add 10 - 20 tests that call your function in different ways,
and show that it can now handle various different conditions and cases.
'''

def check_equality():
	'''compares the value of three numbers to each other'''
	try:
		a = int(input('First #: '))
		b = int(input('Second #: '))
		c = int(input('Third #: '))

		if a == b or a == c or b == c:
			return True
		else:
			return False

	except NameError:
		print('You must always enter a number. Please try again.')



print(check_equality())
