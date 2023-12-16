#21.	The products.csv file contains data about the products sold. Create the file in a text editor.
#Product,Quantity,Price
#milk,8,4.25
#cheese,5,17.90
#bread,21,6.15
#juice,12,5.90
#Then, write a program to convert data from CSV to JSON. The program reads product data from the CSV file and writes the data to a JSON file.

import json
import csv

file = open("products.csv")
csv_reader = csv.DictReader(file)
line_count = 0
values = []
for line in csv_reader:
    values.append(line)

#print(values)
new = open("products.json","w")
data = json.dumps(values, indent=4)
new.write(data)

#new.close()
file.close()
new.close()