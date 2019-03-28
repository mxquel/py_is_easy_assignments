# -----------------------------------------------------------------------------------
# HOMEWORK #4: LISTS
# -----------------------------------------------------------------------------------
'''Create a function that allows you to add things to a list.
Anything that's passed to this function should get added to myUniqueList,
unless its value already exists in myUniqueList.

(If the value doesn't exist already, it should be added and the function should return True.
If the value does exist, it should not be added, and the function should return False)

Add some code below that tests the function, showcasing the different scenarios,
and then finally print the value of myUniqueList

extra: Add another function that pushes all the rejected inputs into a separate global array
called myLeftovers.
'''


myUniqueList = []
myLeftovers = []

def compile_unique_list(item):
	'''depending on uniqueness, allocate item to myUniqueList or myLeftovers'''

	if item not in myUniqueList:
		myUniqueList.append(item)
		return True
	else:
		myLeftovers.append(item)
		return False


# test entries
compile_unique_list('dog')
compile_unique_list(4)
compile_unique_list(True)
compile_unique_list(4)
compile_unique_list('lucky')

# print both lists
print('Unique list:', myUniqueList)
print('Left-overs:', myLeftovers)
