# -----------------------------------------------------------------------------------
# HOMEWORK #10: IMPORTING
# -----------------------------------------------------------------------------------
'''Pick any library that come with Python (https://docs.python.org/3/library/) that
we haven't covered in the course already.

Learn how to use the library extensively, then prepare a code sample that showcases
what you've learned. This can take any form you wish. You could create an application
with the library, or just show examples of how to use its methods.
'''

# chosen re to identify if a pattern is contained in a text or not
import re

def import_text(file_name):
    with open(file_name, 'r') as f:
        return f.read()


interview = import_text('cookie_interview.txt')

def add_headline(headline):
    print('-'* 45, headline, '-'* 45, sep='\n')


# find simple match at the beginning of a string
add_headline('MATCH')

if re.match(r'Cookie', interview):
    print('This definitely starts promisingly with Cookie.')
else:
    print('Sadly, no Cookie found.')

# find first occurance of a pattern where there is either zero or one  anywhere in a string
add_headline('SEARCH')

result = re.search(r'cookies?', interview)
if result:
    txt = 'This definitely contains at least one cookie or cookies.'
    txt += '\nIt was found at {} and endet at {}'
    print(txt.format(result.start(), result.end()))
else:
    print('Sadly, no cookie(s) found.')

print('Word found:', interview[result.start():result.end()])

# find all (non-overlapping) instances of pattern regardless of their case
add_headline('FIND ALL')
result = re.findall(r'cookies?', interview, flags=re.IGNORECASE)

print('Cookie(s) are mentioned', len(result), 'times.')


# substitute the found pattern with something else
add_headline('SUBSTITUTION')
healthy = re.sub(r'cookies?', 'salad', interview)
print(healthy)


# split the string at a particular pattern
add_headline('SPLITTING')
me = 'Max'.join(re.split(r'Cookie\sMonster', interview))
print(me)
