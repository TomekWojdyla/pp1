def binary_check(i):
    binary_str = str(i)
    lent = len(binary_str)
    for i in range (lent):
        if binary_str[i] == "0" or binary_str[i] == "1":
            check = True
        else:
            check = False
            break
    return check

#g = binary_check(1000101011)
#print(g)
#h = binary_check(1101002000)
#print(h)
#h = binary_check("1101002000")
#print(h)
#k = binary_check("11jk11100")
#print(k)