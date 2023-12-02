#24.	A computer program analyses the price of a product in an online store. If the product price decreases by at least 10%, the program displays a purchase recommendation:
#Buy the product!!
#Product price reduced by 17%
#Create such program. The current and previous price of the product are included in the variables. Sample result:
#Current product price: 140.00
#Previous product price: 200.00
#Buy the product!!
#Product price reduced by 30%

current=float(input("Current Product price: "))
previous= float(input("Previous Product price: "))
reduction = (previous-current)/previous*100
if reduction>=10:
    print("Buy this product!")
    print(f"Product price reduced by {reduction:.2f}%")
elif reduction<=10 and reduction >0:
    print("Consider buying this product")
    print(f"Product price reduced by {reduction:.2f}%")
else:
    print("Run away!!!")
    print(f"Product price increased by {-reduction:.2f}%")