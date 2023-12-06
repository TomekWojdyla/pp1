# 34.	Define the function f(n), which returns numbers from 1 to n as a string. Sample result:
#f(11) returns "1234567891011"
#f(4) returns "1234"

def ciag(n):
    i=1
    prnt = ""
    while i<n+1:
        prnt += str(i)
        i += 1
    return prnt

a = int(input("Enter value: "))
g=ciag(a)
print(g)