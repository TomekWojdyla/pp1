def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()
    
#fib(20)

def test(k):
    a=0
    while a<=k:
        print(a, end=" ")
        a=a+1
    print()
    
#test(5)