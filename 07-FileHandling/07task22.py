#22.	Create a program that writes 50 random integers between 100 and 999 to a text file, each number on a separate line.

file1 = open("50randomintegers.txt", "a")

import random

for i in range(50):
    a = str(random.randint(100,999))+"\n"
    file1.write(a)
    
file1.close()

