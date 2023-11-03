#42.	Write a program that allows you to enter a binary, four-digit number. Convert the entered number from binary to decimal value. Do not use available Python functions. Sample result:
#Enter binary number: 0110
#Binary number in decimal notation: 6

bin_str = input("Enter 4-digit binnary number: ")
decimal = int(bin_str[0:1])*2**3+int(bin_str[1:2])*2**2+int(bin_str[2:3])*2**1+int(bin_str[3:4])*2**0
print("Binary number in decimal notation equals: ", decimal)