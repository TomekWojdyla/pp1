# 23.	Create a program that saves to a text file integer numbers in the range <1,10> with their second and third power. Sample result:
#1,1,1
#2,4,8
#3,9,27
#4,16,64
#…

file1 = open("integer_powers.txt", "a")

a = 1
for i in range(10):
    disp = ""
    for j in range(3):
        b = a**(j+1)
        disp += str(b)+","
    file1.write(disp+"\n")
    a +=1

file1.close()

