#52.	Define a function power(x, n) that calculates xn. Apply recursion. Then, calculate 5^3.
#tip: xn =  x * xn-1

def powering(x,y):
    if y==0:
        return 1
    if y==1:
        return x
    if y>1:
        return x*powering(x,y-1)
    
g = powering(5,3)
print(g)
g = powering(2,10)
print(g)