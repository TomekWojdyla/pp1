#11.	Write a program that checks whether the number entered from the keyboard is even or odd. Sample result:

numb=int(input("Enter a number: "))
reminder = numb%2
if reminder==0:
    print(f"{numb} is even number")
else:
    print(f"{numb} is odd number")