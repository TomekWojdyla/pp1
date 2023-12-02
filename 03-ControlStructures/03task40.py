#40.	The 'university' variable contains the name of university where you are studying. Write a program that displays the contents of the variable with an extra space between characters (add a space between each character). Sample result:
#Krakow University of Economics
#K r a k o w   U n i v e r s i t y   o f   E c o n o m i c s 

university = input("Enter name of your university: ")

length=len(university)
#print(length)
#print(university[0])
disp = ""
#for i in range (0,length+1):
#    disp += university[i] +" "
i=0
while i<=length-1:
    a=university[i]
    disp += a + " "
    i += 1
print(disp)