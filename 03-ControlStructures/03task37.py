#37.	Write a program that creates the following pattern. Sample result:
#* 
#* * 
# * * 
#* * * * 
#* * * * * 
#* * * * 
#* * * 
#* * 
#*
b="* * * * * "
a=""
for i in range(1,10):
    if i<=5:
        a=a+"* "
        print(a)
    else:
        print(a[0:10-2*i])