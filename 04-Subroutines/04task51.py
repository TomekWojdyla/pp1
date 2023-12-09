#51.	Define a function sum(n) that for the given natural number n calculates the sum of all natural numbers between 1 and n. Apply recursion. Then, create a program that calculates the sum of natural numbers in the range <1,10>.


def recur_sum(x,y):
    if x-y==0:
        return x+x
    elif y-x==1:
        return y+x
    else:
        return y+recur_sum(x,y-1)
    
g = recur_sum(1,11)
print(g)