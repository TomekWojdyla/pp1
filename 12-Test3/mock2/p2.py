#(p2.py) Create a function f(x,y,d) that returns true when the string of digits d appears in any number between x and y. Otherwise, the function returns false.  Example:
#f(10,15,"14")  True
#f(100,120,"11")  True
#f(205,210,"04")  False
import re

def f(x,y,d):
    check = False
    for i in range(x,y):
        a = re.findall(d,str(i))
        if a!=[]:
            check = True
            break
        else:
            pass
    return check
            
a = f(10,15,"14") 
print(a)
b = f(100,120,"11") 
print(b)
c = f(205,210,"04")
print(c)