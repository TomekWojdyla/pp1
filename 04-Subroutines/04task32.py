#32.	Define the function f(n1,n2,n3), which returns True if at least one of the numbers n1,n2,n3 is negative or False otherwise. Sample result:
#f(11,6,-4) returns True
#f(5,4,14) returns False

def negative(x,y,z):
    if x<0 or y<0 or z<0:
        check = True
    else:
        check = False
    return check

n1 = int(input("number 1: "))
n2 = int(input("number 2: "))
n3 = int(input("number 3: "))

g=negative(n1,n2,n3)
print(g)