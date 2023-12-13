f = open("plik19", "r")
w = open("plik19output", "w")

for line in f:
    w.write(line)
f.close()
w.close()


