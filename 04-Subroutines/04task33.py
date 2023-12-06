# 33.	Define a function f(n) that returns a string of n asterisks, separated by a slash sign. Sample result:
#f(4) returns "*/*/*/*"
#f(1) returns "*"

def asterix(n):
    prnt=""
    i=1
    while i<n+1:
        prnt += "*/"
        i += 1
    prnt = prnt[0:len(prnt)-1]
    return prnt

a = int(input("podaj n"))

g=asterix(a)
print(g)