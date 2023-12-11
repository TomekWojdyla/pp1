#21.	The products.csv file contains data about the products sold. Create the file in a text editor.
#Product,Quantity,Price
#milk,8,4.25
#cheese,5,17.90
#bread,21,6.15
#juice,12,5.90
#Then, write a program to convert data from CSV to JSON. The program reads product data from the CSV file and writes the data to a JSON file.

import json

org = open("products.csv")
org_content = org.read()
print(org_content)

for i in range(1):
    
    
new = open("products_new.json","a")



new.close()
org.close()