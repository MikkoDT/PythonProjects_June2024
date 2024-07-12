text = "  hello world!  "
stripped_text = text.strip()
print(stripped_text)

with open('data.txt','r') as file:
    lines = file.readlines()

print(lines)
for line in lines:
    print(line.strip())