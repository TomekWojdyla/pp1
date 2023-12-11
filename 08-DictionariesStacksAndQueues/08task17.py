#17.	Write a program that spells any text entered from the keyboard, using ICAO spelling alphabet:
#https://en.wikipedia.org/wiki/NATO_phonetic_alphabet
#Create a dictionary in which you put all the letters and the corresponding words. Then, try to spell your name and three other words. Sample result:
#Enter text: uek
#Spelled text: Uniform Echo Kilo

import json

with open("ICAO.json") as icao:
    spelling = json.load(icao)
    
word = input("Enter word to translate to ICAO: ")
lent = len(word)
disp = ""
for i in range(lent):
    if word[i] ==" ":
        disp += "space_sign "
    else:
        sign = word[i]
        disp += spelling[(sign)] +" "

print(f"ICAO spelled word is: {disp}")

