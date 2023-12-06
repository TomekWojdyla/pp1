# 35.	Two numbers and an operator are given. Define a function f(number1,number2,operator) that returns the result of an arithmetic operation. The available operators are +,-,*,%,**. Sample result:
#f(2,3, "+") returns 5
#f(2,3, "%") returns 2
#f(2,3, "**") returns 8
#f(2,3, "*") returns 6
#f(2,3, "-") returns -1

import operator

def operation(a,b,c):
    ops = {"+":operator.add, "-":operator.sub,"*":operator.mul,"%":operator.mod,"**":operator.pow}
    g = ops[c](a,b)
    return g

n=operation(2,3,"+")
print(n)
n=operation(2,3,"%")
print(n)
n=operation(2,3,"**")
print(n)
n=operation(2,3,"*")
print(n)
n=operation(2,3,"-")
print(n)
#x = int(input())