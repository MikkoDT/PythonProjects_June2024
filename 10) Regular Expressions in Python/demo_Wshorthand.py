import re
text = "The quick brown fox jumps over the lazy dog."
pattern = r"\W"
matches = re.findall(pattern,text)
print(matches)