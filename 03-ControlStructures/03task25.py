#25.	In one of the online stores, a 25% discount is charged for each product purchased over two. Write a program that calculates the amount to be paid. Read the number of purchased products and the product price from the keyboard. Sample result:
#Number of products purchased: 5
#Product price: 40
#Amount to pay: 170.00


count = int(input("Number of products purchased: "))
price = float(input("Product price: "))
if count>2:
    tot = 2.0*price + (count-2)*(price*0.75)
else:
    tot = count*price
print("Your total is: ",tot)