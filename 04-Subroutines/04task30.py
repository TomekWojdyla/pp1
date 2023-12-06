#30.	Create a function f(number, even) that computes the sum of the digits of a number. When the value of the even parameter is True, the function returns the sum of the even digits. When the value of the even parameter is False, the function returns the sum of the odd digits. Sample result:
#f(3124,True) returns 6
#f(3124,False) returns 4
#f(20576,False) returns 12
#f(20576,True) returns 8
#f(13115,True) returns 0

def fancy_sum(x,y):
    sum = 0
    n=str(x)
    if y==True:
        for i in range(0,len(n)):
            if int(n[i])%2 ==0:
                sum += int(n[i])
            else:
                pass
    else:
        for i in range(0, len(n)):
            if int(n[i])%2 ==0:
                pass
            else:
                sum += int(n[i])
    return sum

g=fancy_sum(3124,True) 
print(g)
g=fancy_sum(3124,False) 
print(g)
h=fancy_sum(20576,False) 
print(h)
k=fancy_sum(20576,True) 
print(k)
l=fancy_sum(13115,True) 
print(l)
m=fancy_sum(13115,False) 
print(m)
#f(3124,False) returns 4
#f(20576,False) returns 12
#f(20576,True) returns 8
#f(13115,True) returns 0

