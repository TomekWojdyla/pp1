# 47.	Define a function f(text) that returns the given text with all characters separated by "-" (minus sign). Example:
#f("Univesity") returns "U-n-i-v-e-r-s-i-t-y"
#f("UE") returns "U-E"
#f("x") returns "x"
#f("") returns ""

def dashes(x):
    y = len(x)
    prnt = ""
    for i in range(0,len(x)):
        prnt += x[i]+"-"
    prnt_y = len(prnt)
    if prnt_y<1:
        pass
    else:
        if prnt[prnt_y-1] == "-":
            prnt = prnt[0:prnt_y-1]
    return prnt


g = dashes("University")
print(g)
g = dashes("UE")
print(g)
g = dashes("x")
print(g)
g = dashes("")
print(g)