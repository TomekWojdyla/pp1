#(p5.py) The binary system uses two symbols to represent a number: 0 and 1. Define a function f(binary_number) that returns True if the given notation is a valid binary number, or false otherwise. Example:
#f("101101") returns True
#f("1311a10100") returns False

def f(bina):
    check = True
    for i in range(len(bina)):
        if bina[i] not in ["0","1"]:
            check = False
    return check

a = f("101101")
print(a)
a = f("1311a10100")
print(a)