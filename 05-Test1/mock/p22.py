#(p2.py) Define the function f(n1,n2,n3) that returns True if all three numbers n1,n2,n3 are different or False otherwise. Sample result:
#f(4,8,5) returns True
#f(2,9,2) returns False

def f(n1,n2,n3):
    if n1==n2 or n2==n3 or n1==n3:
        return False
    else:
        return True

a = f(4,5,5)
print(a)
a = f(1,2,2)
print(a)