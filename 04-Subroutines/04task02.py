#2.	In addition to the built-in functions, you can use numerous functions available in ready-to-use modules. One example is the 'math' module.
#https://docs.python.org/3/library/math.html 
#Using functions and constants available in the 'math' module, write a program that calculates and displays:
#a.	natural logarithm of 5
#b.	e raised to the power of 3
#c.	square root of 7
#d.	sine of 90 degrees

import math

print("natural logarithm of 5 is: ", math.log1p(5-1))
print("natural logarithm of 5 is also: ", math.log(5))

print("e raised to the 3rd power is: ", math.exp(3))

print("square root of 7 is: ", math.sqrt(7))

radians_of_90 = 90*2*math.pi/360
print("sine of 90 deg is: ", math.sin(radians_of_90))