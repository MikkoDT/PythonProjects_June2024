import re

string = "andy"
pattern = r"^an"

if re.match(pattern, string):
    print('Match found.')
else:
    print('No match found.')