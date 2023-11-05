#13.	A user enters two integer numbers from the keyboard. Write a program that checks whether at least one of them is not negative. Sample result:

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if num1>=0 or num2>=0:
    print("At least one number is NOT negative.")
else:
    print("Both provided numbers are negative.")
    