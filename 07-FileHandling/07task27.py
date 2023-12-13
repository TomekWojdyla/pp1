# 27.	Write a program that computes the number of words in the following text. Use regular expressions.
#To be, or not to be, that is the question

import re
text = "To be, or not to be, that is the question"
words = re.findall(r"\b[a-zA-Z]+\b",text)
print(words)
