import re
text = "Helloooooo, Python is awesomeeeee!"
pattern = r"\w*o+\w*"
#\w*: Matches zero or more alphanumeric characters
#o+: Matches one or more occurrences of the letter 'o'
matches = re.findall(pattern,text)
print(matches)