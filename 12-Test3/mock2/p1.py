#(p1.py) Create a function f(n) that returns the difference between the largest and smallest odd digit contained in the number n. When the number n does not contain odd digits, the function returns -1. Example:
#f(10852)  4
#f(7235973)  6
#f(4388)  0
#f(846206)  -1

def f(n):
    string = str(n)
    lent = len(string)
    odd = []
    for i in range(lent):
        dig = int(string[i])
        if dig%2 ==0:
            pass
        else:
            odd.append(int(string[i]))
    if odd==[]:
        outp = -1
    else:
        odd.sort()
        outp = odd[-1]-odd[0]
    return outp

a = f(10852)
print(a)
a = f(7235973)
print(a)
a = f(4388)
print(a)
a = f(846206)
print(a)
