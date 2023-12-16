def f(e):
    lent= len(e)
    sum=int(e[0])
    for i in range(1,lent-1,2):
        if e[i]=="-":
            sum = sum -int(e[i+1])
        else:
            sum = sum + int(e[i+1])
    return sum


g= f("2+3")
print(g)
g = f("2+3-4+5-0")
print(g)
g = f("1+1+1+1-1-1-1-1")
print(g)

