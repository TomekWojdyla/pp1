# 31.	Define the function f(x,y) that returns the number of negative even numbers in the range <x,y>. Sample result:
#f(-7,8) returns 3
#f(-1,11) returns 0

def odd_count(x,y):
    count = 0
    for i in range(x,y+1):
        if i%2==0 and i<0:
            count += 1
        else:
            pass
    return count

n=int(input("Enter lower rande end: "))
m=int(input("Enter higher rande end: "))

g=odd_count(n,m)
print(g)