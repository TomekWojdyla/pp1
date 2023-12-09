#40.	Define a function f(number) that returns the sum of repeated digits in a number. Sample result:
#f(1027) returns 0
#f(230335) returns 9
#f(513553007) returns 21 

def repeat(x):
    sum = 0
    y = str(x)
    check = []
    for i in range (0,10):
        a=0
        for j in range (0, len(y)):
#            b=y[j]
#            g = i==y[j]
            if str(i) == y[j]:
                a += 1
            else:
                pass
        check.append(a)
    for i in range (0,10):
        if check[i]>1:
            sum += check[i]*i
        else:
            pass
    return sum

g = repeat(1027)
print(g)
g = repeat(230335)
print(g)
g = repeat(513553007)
print(g)