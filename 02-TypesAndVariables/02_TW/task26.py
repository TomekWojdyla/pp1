#26.	Write a program that checks whether the number entered from the keyboard is even. Display True when the number is even and False when the number is odd.
entry = input("Enter natural number to check (other than 0):")
number = int(entry)
reminder = number%2
print("Number is even:", reminder==0)
#condition to check if enetered value equals zero could be added