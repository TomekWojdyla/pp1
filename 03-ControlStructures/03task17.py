# 17.	Write a program that calculates the sum of integer numbers in the range <1,5>. Use the "while" statement.

i=1
sum=0
while i<=5:
    print(i)
    sum = sum+i
    i=i+1
print("Summation in range<1,6> equals: ", sum)

#to samo ale for

sum2=0
for i in range(1,6):
    print(i)
    sum2=sum2+i
print("Summation 2 in range<1,6> equals: ", sum2)