import re

string = "pythonfile"
pattern = r"python-?file"

if re.match(pattern, string):
    print('Match found.')
else:
    print('No match found.')