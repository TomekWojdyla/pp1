import random as rd

f = open("plik22", "w")

for i in range(50):
    liczba = rd.randint(100,999)
    f.write(str(liczba) + '\n')
f.close()
