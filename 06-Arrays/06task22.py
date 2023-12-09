# 22.	Create a program that computes the second power of each array element. Sample result:
#Array: 8 2 5 1 9
#2nd power: 64 4 25 1 81

import math

array = [8,2,5,1,9]
z = len(array)
for i in range(z):
    array[i] = array[i]**2
print(array)