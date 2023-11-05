#12.	Using built-in Python functions, write a program that calculates and displays:
#a.	the largest number given: 7,5,6,3,8,2
#b.	binary string representing decimal number 304
#c.	hexadecimal string representing decimal number 304
#d.	integer representing the Unicode code of the € sign
#e.	absolute value of -17

# task a
max_number = max(7,5,6,3,8,2)
print('Max number of 7,5,6,3,8,2 is', max_number) 

# task b
binary = bin(304)
print("binary representation of 304 is: ", binary)

# task c
hexadecimal = hex(304)
print("hexadecimal representation of 304 is: ", hexadecimal)

# task d -> tego nie umiem
#unicode = ord(€)
#euro = "\N{euro sign}"
#print = ("\N{euro sign}")
#print("Unicode representation of € is: ", unicode)

# task e
print("absolute value of -17 is: ", abs(-17))


