#14.	Write a program that allows you to add a name of next product you want to buy at the end of the shopping.txt file. Enter the product name from the keyboard. Numbers products on the list. Tip: open the file in appending mode. Sample result:
#ile = open("shopping.txt",…)
#read_product = True
#counter = 0
#while read_product:
##    product = input("Enter product name: ")
#    if product != "":
#        counter += 1
#        file.write(…)
#    else:
#        read_product = False
#file.close()
#shopping.txt
#1. Milk
#2. Bread
#3. Fish
#4. Water
#5. Cheese

shoplist=open("shop_list_tw.txt", "a")
read_product=True
number =0
while read_product==True:
    product=input("Enter new product to list: ")
    if product !="":
        number += 1
        shoplist.write(str(number) + " " + product + "\n" )
    else:
        read_product=False
shoplist.close()
