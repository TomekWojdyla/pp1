# 37.	Define the function f(n), which returns the n-th value of the Fibonacci sequence. The sequence is defined as follows: the first value of the sequence is 0, the second value is 1. Each subsequent value is the sum of the previous two. Sample result:
#f(5) returns 3
#f(9) returns 21


def fibonaci(n):
    array = [0,1]
    if n==0 or n==1:
        pass
    else:
        for i in range(2,n):
            array.append(array[i-2]+array[i-1])
    return array[n-1]

g = fibonaci(5)
print(g)
h = fibonaci(9)
print(h)
