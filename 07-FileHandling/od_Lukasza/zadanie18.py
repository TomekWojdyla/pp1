f =open("plik18.txt","r")
text = f.read()
w = open("copy.txt", "w")
w.write(text)

f.close()
w.close()


# 1. otwieramy pierwszy plik do odczyty
# 2. korzystamy z metody read i zapisujemy całą  zawartosc pliku  do zmiennej
# 3. otwieramy plik do zapisu w trybie "w"
# 4. korzystamy z metody write i zapisujemy do pliku wyjsciego zawartosc contentu pliku wejsciowego
# 5. ZAMYKAMY OBA PLIKI!!!


