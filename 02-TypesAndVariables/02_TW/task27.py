# 27.	Write a program that checks whether the number entered from the keyboard is between -10 and 10. Display True if the number is in the given range, and False otherwise. 
entry = input("Enter number to check:")
number = float(entry)
#range_check = number >= -10 and number <= 10
#print("Number is in the range <-10,10>:", range_check)
print("Number is in the range <-10,10>:", number >= -10 and number <= 10)