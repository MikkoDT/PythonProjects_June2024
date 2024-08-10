import re
text = "The quick brown fox jumps over the lazy dog."
pattern = r"\D"
matches = re.findall(pattern,text)
print(matches)