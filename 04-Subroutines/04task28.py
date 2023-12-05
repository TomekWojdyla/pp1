#28.	The binary numerical system uses two symbols to represent a number: 0 and 1. Define a function f(binary_number) that returns True if the given string of digits is a valid binary number, or False otherwise. Sample result:
#f("101101") returns True
#f("1311a10100") returns False

def binary_check(n):
    a = str(n)
    b = len(a)-1
    i=0
    while i<=b:
        if a[i]=="0" or a[i]=="1":
            check = True
            i += 1
        else:
            check = False
            i +=1
            pass
    return check
    
number = input("Enter binary number: ")
validation = binary_check(number)
print(f"Provided number is binary: {validation}")

