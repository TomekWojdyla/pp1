#42.	Define the function f(number1,number2,number3), which returns the difference between the largest and smallest numbers. Sample result:
#f(7,4,9) returns 5
#f(2,12,8) returns 10


def diff (n1, n2, n3):
   maximum = max(n1, n2, n3)
   minimum = min(n1, n2, n3)
   
   sum = maximum - minimum
   return sum

g = diff(7,4,9)
print(g)
g = diff(2,12,8)
print(g)
        
    
    