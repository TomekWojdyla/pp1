# 48.	Products are marked with a special code consisting of 3 digits and a fourth control digit. The forth digit is determined by calculating the remainder of dividing the sum of the first three digits by 7. Define a function f(product_code) that returns True if the product code is correct or False otherwise. Sample result:
#f("1082") returns True
#f("2035") returns True
#f("1114") returns False
#f("7071") returns False

def check(x):
    y = str(x)
    sum = int(y[0])+int(y[1])+int(y[2])
    #print(sum)
    #print(sum%7)
    if sum%7 == int(y[3]):
        val = True
    else:
        val = False
    return val

g = check(1082)
print(g)
g = check(2035)
print(g)
g = check(1114)
print(g)
g = check(7071)
print(g)