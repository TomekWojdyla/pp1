def f(n):
    a = n//5
    b = (n-5*a)//2
    c = (n-5*a-2*b)//1
    sum = a+b+c
    return sum

#g = f(23)
#print(g)

#h = f(8)
#print(h)

if __name__ == '__main__':
    #check your program in this place
    print(f(9))
    print(f(10))
    print(f(16))