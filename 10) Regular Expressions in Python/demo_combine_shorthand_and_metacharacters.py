import re
text = "Helloooooo, Python is awesomeeeee!"
pattern = r"\w*o+\w*"
matches = re.findall(pattern,text)
print(matches)