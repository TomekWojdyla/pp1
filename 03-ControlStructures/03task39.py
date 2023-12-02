#39.	The variables a and b contain the dimensions of the sides of the rectangle. Write a program that creates the following rectangle with dimensions a and b. Sample result for a = 4 and b = 15:
#***************
#*             *
#*             *
#***************

a=int(input("Podaj liczbe wierszy: "))
b=int(input("Podaj liczbe kolumn: "))

for i in range(1,a+1):
    disp=""
    if i==1 or i==a:
        for j in range (1,b+1):
            disp += "* "
        print(disp)
    else:
        for j in range (1, b+1):
            if j==1 or j==b:
                disp += "* "
            else:
                disp += "  "
        print(disp)