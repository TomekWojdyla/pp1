# 43.	A variable contains text:
#An apple a day keeps the doctor away
#Create a module MyText, containing:
#a.	A function that returns the number of words in the text
#b.	A function that returns an ordered array of words, from longest to shortest
#c.	A function that returns an alphabetically ordered array of words
#Then, write a program, call the functions and display results. Sample result:
#Text: An apple a day keeps the doctor away
#Number of words: 8
#Words from the longest: doctor,apple,…
#Words ordered alphabetically: a,An,apple,away,…

var_text = "An apple a day keeps the doctor away"

import MyText_tw

g = MyText_tw.word_count(var_text)
print(g)

g = MyText_tw.word_ordered(var_text)
print(g)

g = MyText_tw.word_alpha(var_text)
print(g)