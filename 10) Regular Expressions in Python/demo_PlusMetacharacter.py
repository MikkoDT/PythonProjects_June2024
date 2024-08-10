import re

string = "abc"
pattern = r"a+bc"

if re.match(pattern, string):
    print('Match found.')
else:
    print('No match found.')