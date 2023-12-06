# 38.	A palindrome is an expression that sounds the same when read backwards. Define a function f(palindrome) that returns True if the expression is a palindrome or False otherwise. Sample result:
#f("radar") returns True
#f("12-11-21") returns True
#f("book") returns False


def palindrom(a):
    n = len(a)
    for i in range (0,len(a)):
        #print(a[i])
        if a[i]==a[n-i-1]:
            check = True
        else:
            check = False
    return check
    
g = palindrom("radar")
print(g)    
g = palindrom("12-11-21")
print(g)   
g = palindrom("book")
print(g)   