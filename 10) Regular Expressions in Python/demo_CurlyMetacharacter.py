import re

string = "abbb"
pattern = r"ab{2,}"

if re.match(pattern, string):
    print('Match found.')
else:
    print('No match found.')