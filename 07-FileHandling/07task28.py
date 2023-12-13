# 28.	Find any text file on the Internet and download it to your computer. Then, write a program that displays all words with at least six letters from the file. Display each word on a separate line. Use regular expressions.

import re

file = open("skydiving.txt")
file_content = file.read()
search = re.findall(r"\b[A-Za-z]{6,}\b",file_content)
print(search)
print(len(search))
#arr = file_content.split()
#print(arr)



#for word in file:
#    print(word)

file.close()