import re

string = "bac"
pattern = "a"

if re.search(pattern, string):
    print('Match found.')
else:
    print('No match found.')