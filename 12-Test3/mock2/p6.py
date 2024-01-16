#(p6.py) A valid number on the planet Metis consists of digits 1 to 7 and lowercase or uppercase letters a to d. A plus (+) or minus (-) sign may also appear at the beginning of the number. The mnumbers array contains sample numbers. Create a function f(mnumbers) that returns how many numbers in the array that are valid in the planet Metis. Example:
#f(["A15","-31","7abC","+D1","-gH"])  5
#f(["A05","-3+1","7ab8C","+D1","-22k"])  1

import re

def f(mnumbers):
    lent = len(mnumbers)
    outp = []
    for i in range(lent):
        a = re.findall(r'\b[+-]?[1-7a-dA-D]{1,7}\b',mnumbers[i])
        if a==[] or len(a)>1: # ten regex można napisac lepiej?? wyszukuje w -3+1 dwa itemy -3 i +1
            pass
        else:
            outp.append(a)
    count = len(outp)
    return count

a = f(["A15","-31","7abC","+D1","-gH"])
print(a)
a = f(["A05","-3+1","7ab8C","+D1","-22k"])
print(a)