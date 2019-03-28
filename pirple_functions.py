# -----------------------------------------------------------------------------------
# HOMEWORK #2: FUNCTIONS
# -----------------------------------------------------------------------------------
'''create 3 functions (with the same name as those attributes), 
which should return the corresponding value for the attribute.

extra: create a function that returns a boolean'''


year_recorded = 2003
artist = 'Snow Patrol'

def show_favorite_band(artist):
	return artist

#function with default
def return_recording_year(year = 1900):
	return year

# function without parameters
def echo_best_song():
	return 'Run'

def search_artist(s):
	'''tests if a substring is part of the artist name'''
	return s in artist

# test functions through print statements
print(f"{echo_best_song()} ({return_recording_year(year_recorded)}) – {show_favorite_band(artist)}")
print("There were no songs released in:", return_recording_year())
print(search_artist('Snow'))
print(search_artist('Sun'))
