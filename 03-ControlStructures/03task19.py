#19.	Write a program that calculates the sum of even numbers in the range <1,10>.

i=1
sum=0
while i<=10:
    if i%2!=0:
        pass
    else:
        sum = sum+i
    i=i+1
print("Sum of even numbers in <1,10> range equals: ", sum)

#to samo ale for
sum2 = 0
for j in range(1,11):
    if i%2!=0:
        pass
    else:
        sum2 = sum2+i
print("Sum2 of even numbers in <1,10> range equals: ", sum)

#for z krokiem
sum3 = 0
for j in range(0,11,2):
        sum3 = sum3+i
print("Sum3 of even numbers in <1,10> range equals: ", sum)