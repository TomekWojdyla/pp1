# 21.	Write a program that displays two numbers entered from the keyboard in ascending order.
#Enter first number: 27
#Enter second number: 14
#Numbers in ascending order: 14, 27

no1 = int(input("Enter first number: "))
no2 = int(input("Enter second number: "))
if no1<=no2:
    print(f"Numbers in ascending order: {no1}, {no2}")
else:
     print(f"Numbers in ascending order: {no2}, {no1}")
     