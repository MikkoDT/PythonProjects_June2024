import re

string = "bc"
pattern = "ab*c"

if re.search(pattern, string):
    print('Match found.')
else:
    print('No match found.')