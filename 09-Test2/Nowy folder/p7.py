def f(d,v):
    lent = len(d)
    check = not v
    counter = 0
    for key,value in d.items():
        if value == check:
            counter +=1
        else:
            pass
    return counter

