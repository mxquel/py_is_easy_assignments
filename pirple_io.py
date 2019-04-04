# -----------------------------------------------------------------------------------
# HOMEWORK #8: INPUT AND OUTPUT (I/O)
# -----------------------------------------------------------------------------------
'''Create a note-taking program:
Prompt a user for a filename.

If the file doesn't exist, prompt them to enter text to write to the file. 
Save the file and exit.

If the file already exists, ask the user if they want:
	a) read the content
	b) overwrite the file
	c) append the file

extra: 
	d) replace the content of a single line
'''

import os.path as osp

instruction = "This file already exists.\n\n"
instruction += "If you would like to read the contents enter: r\n"
instruction += "If you would like overwrite please enter: w\n"
instruction += "If you would like to add text please enter: a\n"


file_name = input('Please enter a file name: ')

if osp.isfile(file_name):
	user_choice = input(instruction)
	user_file = open(file_name, user_choice)
	
	if user_choice == 'w' or user_choice == 'a':
		user_file.write(input('Enter your text: ') + '\n')
		user_file.close()
	else:
		print(user_file.read())
		user_file.close()
else:
	user_file = open(file_name, 'w')
	user_file.write(input('Enter your text: '))
	user_file.close


