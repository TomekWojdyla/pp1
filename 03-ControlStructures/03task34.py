#34.	There are coins of 1, 2 and 5 Polish Zlotys (PLN). Write a program showing any amount (natural number) read from the keyboard with as few coins as possible.
#Enter the amount in PLN: 18
#The amount of PLN 18 in coins:
#5 zł – 3 
#2 zł – 1 
#1 zł – 1

price = int(input("Amount to pay in PLN: "))
a=price//5
b=(price%5)//2
c=((price%5)%2)
print(f"The amount of {price} PLN in 5,2,1 coins is as follows:")
print("5 PLN: ",a)
print("2 PLN: ",b)
print("1 PLN: ",c)