f  = open("plik17", 'r')

licznik = 0

for line in f:
    print(line, end="")
    licznik += 1
    if licznik % 5 == 0 and licznik > 0 and licznik < 26:
        input("Wcisnij enter zeby kontynowac: ")
