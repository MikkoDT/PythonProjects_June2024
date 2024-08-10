import re

string = "ABCD"
pattern = r"[a-z]"

if re.match(pattern, string):
    print('Match found.')
else:
    print('No match found.')