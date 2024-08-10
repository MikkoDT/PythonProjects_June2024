import re
text = "The cat and the dog sat on the mat."
pattern = r"[xyz]"
matches = re.findall(pattern,text)
print(matches)