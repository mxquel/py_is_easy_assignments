# -----------------------------------------------------------------------------------
# HOMEWORK #7: DICTIONARIES AND SETS
# -----------------------------------------------------------------------------------
'''refactor the code from first assigment so every variable and its corresponding value
become key value pairs in a dictionary. then loop through each item in the dictionary
to print out the key and value

extra: Create a function that allows someone to guess the value of any key in the dictionary,
and find out if they were right or wrong.
This function should accept two parameters: Key and Value. If the key exists
in the dictionary and that value is the correct value, then the function should return True.
In all other cases, it should return False
'''

favorite_song = {
    'title': 'Run',
    'released': (2004, 1, 26),
    'year recorded': 2003,
    'artist': 'Snow Patrol',
    'album': 'Final Straw',
    'b-side': 'Post Punk Progression',
    'genre': 'Indie',
    'labels': ['Fiction Records', 'Polydor'],
    'producer': 'Jacknife Lee',
    'song writers': ['Gary Lightbody', 'Jonathan Quinn', 'Mark McClelland', 'Nathan Connolly', 'Iain Archer'],
    'studios': {'London': 'Britannia Row Studios', 'Glasgow': 'The Divining Bell Longue Studios'},
    'lengths in min': {'album': 5.93, 'radio edit': 4.27}
}

# print where values are strings, numbers or tuples:
[print(f"* {k.title()}: {v}") for k, v in favorite_song.items() if isinstance(v, (str, int, tuple))]

# print where values are lists or dictionaries
[print(f"* {k.title()}: {(', '.join(v)).title()}") for k, v in favorite_song.items() if isinstance(v, (list, dict))]
