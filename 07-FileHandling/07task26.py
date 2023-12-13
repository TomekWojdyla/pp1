# 26.	Write a program that calculates the number of vowels in the text:
#To be, or not to be, that is the question
#Use regular expressions and the findall() method.

import re

snet = "To be, or not to be, that is the question"
vovels = ["a","e","i","o","u","y"]
vovels_in_text = re.findall("[aeiouy]",snet)
#print(vovels_in_text)
print(len(vovels_in_text))