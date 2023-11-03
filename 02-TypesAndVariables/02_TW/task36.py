# 36.	A bank buys and sells Euro. Write a program that, based on the Euro buying and selling rates entered from the keyboard, calculates the difference between the buying and selling rates (spread). Display result with 4 decimal places. Sample result:
#Bank buys EUR: 4.5940
#Bank sells EUR: 4.6250
#Spread: 0.0310


purchase_price_str = input("Enter EUR purchase price in bank: ")
purchase_price = float(purchase_price_str)
sell_price_str = input("Enter EUR selling price in bank: ")
sell_price = float(sell_price_str)
spread = sell_price - purchase_price
spread_f = f"{spread:.4f}"
print("Spread equals: ", spread_f)