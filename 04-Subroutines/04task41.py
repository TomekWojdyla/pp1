#41.	Define the function f(n) that returns the n-th prime number. A prime number is a natural number greater than 1, divisible by 1 and that number. Sample result:
#f(1) returns 2
#f(5) returns 11


def prime(n):
    prime_count = 0
    j=1
    while prime_count<=n:
        #look for prime numbers
        div = 0
        for i in range(1,j+1):
            if j%i == 0:
                div +=1
            else:
                pass
        if div>2:
            check = False
            j +=1
        else:
            check = True
            prime_count += 1
            j +=1
    return j-1

g = prime(4)
print(g)