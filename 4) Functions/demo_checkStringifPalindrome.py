word = "python"
#print(word[5])

l = len(word)

#Looping through the letters
palindrome_flag = True
for i in range(l):
    if word[i] != word[l-i-1]:
        palindrome_flag = False
        break
    else:
        palindrome_flag = True

if palindrome_flag:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

