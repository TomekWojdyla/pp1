f = open("plik23.1", "w")

for i in range(1,11):
    liczba = str(i)
    kwadrat = str(i*i)
    szescian = str(i*i*i)
    f.write(liczba + "," + kwadrat + "," + szescian + "\n")

f.close()