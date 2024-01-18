#(p6.py) Create a function f(number, even) that computes the sum of the digits of a number. When the value of the even parameter is True, the function returns the sum of the even digits. When the value of the even parameter is False, the function returns the sum of the odd digits. Example:
#f(3124,True) returns 6
#f(3124,False) returns 4
#f(20576,False) returns 12
#(20576,True) returns 8
#(13115,True) returns 0


def f(no,ev):
    word = str(no)
    sum=0
    if ev == True:
        for i in range(len(word)):
            if int(word[i])%2==0:
                sum+=int(word[i])
            else:
                pass
    else:
        for i in range(len(word)):
            if int(word[i])%2!=0:
                sum+=int(word[i])
            else:
                pass
    return sum

a = f(3124,True)
print(a)
a = f(3124,False)
print(a)
a = f(20576,False)
print(a)
a = f(20576,True)
print(a)
a = f(13115,True)
print(a)