#39.	The price of the product on the price tag is given before and after the discount is applied. Write a program that allows you to enter the product price and discount. Display the product price, discount, discounted product price, and the difference between the product price before and after the discount. Display all prices with two decimal places. Sample result:
#Enter price: 24.72
#Enter discount %: 15
#Price with discount: 21.01
#eduction: 3.71


price_str = input("Enter original product price: ")
price = float(price_str)
discount_str = input("Enter discount percentage [%]: ")
discount = float(discount_str)
#mozna dodać warunek czy <100
price_after_discount = price*(100-discount)/100
price_red = price-price_after_discount
#print("Price of product after discount: ", price_after_discount)
#print("Reduction of price: ", price_red)
print("Price of product after discount: ", f"{price_after_discount:.2f}")
print("Reduction of price: ", f"{price_red:.2f}")