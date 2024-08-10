import re
text = "Please contact me at john@example.co or via email at jane@example.com"
# john@example.com

pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"

matches = re.findall(pattern,text)
print(matches)