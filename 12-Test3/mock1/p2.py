#(p2.py) Create a function f(x,y,digit) that returns how many times the given digit appears in numbers in the range from x to y. Example:
#f(10,15,1)  7
#f(28,32,2)  3
#f(100,105,6)  0
#f(100,101,0)  3

def f(x,y,digit):
    counter = 0
    for i in range(x,y+1):
        word = str(i)
        lent = len(word)
        for j in range(lent):
            if word[j]==str(digit):
                counter +=1
            else:
                pass
    return counter

a = f(10,15,1)
print(a)
a = f(28,32,2)
print(a)
a = f(100,105,6)
print(a)
a = f(100,101,0)
print(a)