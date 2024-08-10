import re

string = "abc"
pattern = "a"

if re.match(pattern, string):
    print('Match found.')
else:
    print('No match found.')