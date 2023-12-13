#21.	Create a program that writes to a text file integer numbers in the range <1,50>, every number in a separate line.

file1 = open("Integers1_50.txt", "a")

a = 1
for i in range(0,50):
    b = str(a)+"\n"
    file1.write(b)
    a +=1

file1.close()