#10.	Write a program to calculate the absolute value of a number entered from the keyboard. Sample result:

num=float(input("Enter a number: "))
if num>=0:
    print(f"|{num}|= {num}")
else:
    print(f"|{num}|= {-num}")