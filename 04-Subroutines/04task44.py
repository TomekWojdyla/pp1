#44.	A valid password should consist of at least six different characters. Define a function f(password) that returns True if the password is correct or False otherwise. Sample result:
#f("ax15") returns False
#f("book123") returns False
#f("A2water3") returns True
#f("qwerty") returns True
#f("") returns False

def f(x):
    y = len(x)
    if y<6:
        val = False
    else:
        for i in range (0,y):
            for j in range (0,y):
                k = x[i]
                h =x[j]
                if i !=j:
                    if x[i] == x[j]:
                        val = False
                        break
                    else:
                        val = True
                else:
                    pass
            if val == False:
                break
            else:
                pass
    return val

g = f("ax15")
print(g)
g = f("book123")
print(g)
g = f("A2water3")
print(g)
g = f("qwerty")
print(g)
g = f("")
print(g)
g = f("567  uiop[]")
print(g)
g = f("wertyuiop[ ]")
print(g)