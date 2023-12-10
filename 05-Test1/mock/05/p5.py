def f(i):
    binary_str = str(i)
    lent = len(binary_str)
    for i in range (lent):
        if binary_str[i] == "0" or binary_str[i] == "1":
            check = True
        else:
            check = False
            break
    return check

#g = f(1000101011)
#print(g)
#h = f(1101002000)
#print(h)
#h = f("1101002000")
#print(h)
#k = f("11jk11100")
#print(k)