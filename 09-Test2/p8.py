def f(x):
    count = 0
    for i in range(1,x+1):
        if x%i==0:
            count +=1
        else:
            pass
    if count>2:
        ans = False
    else:
        ans = True
    return ans

g = f(7)
print(g)
g = f(21)
print(g)
g = f(19)
print(g)