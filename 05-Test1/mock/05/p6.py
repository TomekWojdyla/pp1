def f(n1, n2):
    n1_str = str(n1)
    sum = 0
    if n2 == True:
        for i in range(0,len(n1_str)):
            if int(n1_str[i])%2 == 0:
                sum += int(n1_str[i])
            else:
                pass
    else:
        for i in range(0,len(n1_str)):
            if int(n1_str[i])%2 != 0:
                sum += int(n1_str[i])
            else:
                pass
    return sum

#g = f(3124,True)
#print(g)
#g = f(3124,False)
#print(g)
#g = f(20576,True)
#print(g)
#g = f(20576,False)
#print(g)
#g = f(13115,True)
#print(g)