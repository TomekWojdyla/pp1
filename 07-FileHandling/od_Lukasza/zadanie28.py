import re

f = open("skydiving.txt", "r")

content = f.read()

slowa = re.findall(r'\b\w{6,}\b',content)

# cos takiego działa: r'\b\w{6,}\b' ???
# w poleceniu było skorzystanie z wyrazen regularnych
# więc to jest jedyny wzor patternu która zwraca słowa o dlugosci równej lub większej niz 6


for i in slowa:
    print(i)
