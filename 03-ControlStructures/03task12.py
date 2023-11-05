#12.	Write a program that checks that two people are adults. Read people’s data from the keyboard. Sample result:

name1 = input("Enter first person name: ")
age1 = float(input("Enter first person age: "))
name2 = input("Enter second person name: ")
age2 = float(input("Enter second person age: "))
if age1>=18 and age2>18:
    print(f"Both {name1} and {name2} are adults")
else:
    print(f"At least one of {name1} and {name2} is NOT adult.")
    