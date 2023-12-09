#45.	An expression contains operators for adding and subtracting single-digit numbers. Define a function f(expression) that returns the value of the expression. Sample result:
#f("2+3") returns 5
#f("3+8+1") returns 12
#f("2+3-4+5-0") returns 6

def f(x):
    y = len(x)
    eq = int(x[0])
    for i in range(2,len(x),2):
        if x[i-1] == "+":
            eq = eq + int(x[i])
        else:
            eq = eq - int(x[i])
    return eq

g = f("2+3")
print(g)
g = f("3+8+1")
print(g)
g = f("2+3-4+5-0")
print(g)        