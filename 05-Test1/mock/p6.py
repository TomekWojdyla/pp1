#Create a function f(number, even) that computes the sum of the digits of a number. When the value of the even parameter is True, the function returns the sum of the even digits. When the value of the even parameter is False, the function returns the sum of the odd digits.

def summation(number, even):
    string = str(number)
    a=len(string)
    sum=0
    i=0
    while i < a+1:
        sum_all=sum+int(a[i])
        i=i+1
    return sum_all

x=3124
y=True
z=summation(x,y)
print(z)

#if __name__ == '__main__':
    #check your program in this place
   # print(f(3124,True))
   # print(f(3124,False))
   # print(f(20576,True))
   # print(f(20576,False))
   # print(f(13115,True))
    