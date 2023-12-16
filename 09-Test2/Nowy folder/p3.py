def f(c):
    lent= len(c)
    sum=0
    for i in range(lent):
        if c[i] in ["T","J","Q","K","A"]:
            sum+=10
        else:
            sum+=int(c[i])
    return sum



