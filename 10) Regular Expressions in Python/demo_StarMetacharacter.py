import re

string = "abbbaaabbbbc"
pattern = "ab*c"

if re.match(pattern, string):
    print('Match found.')
else:
    print('No match found.')