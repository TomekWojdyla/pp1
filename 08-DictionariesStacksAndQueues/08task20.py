#20.	The website http://api.nbp.pl contains data on exchange rates published by the National Bank of Poland. The service provides data in json or xml formats. Display the last ten Euro exchange rates in json format in the browser window. Save the data to the euro.json file. Then, write a program that displays the data from the euro.json file in the following format:

#Date            Buying Rate     Selling Rate
#============================================
#2019-10-25      3.8150          3.9820
#...             ...             ...

import json
print("Date            Buying Rate     Selling Rate")
print("============================================")

eur_json = open("euro.json")
eur_content = json.load(eur_json)

#"rates":[{"no":"230/C/NBP/2023","effectiveDate":"2023-11-28","bid":4.3104,"ask":4.3974}

rates_all = eur_content["rates"]
lent = len(rates_all)
for i in range(lent):
    a = str(rates_all[i]["effectiveDate"])
    b = str(rates_all[i]["bid"])
    c = str(rates_all[i]["ask"])
    disp = a+"      "+b+"          "+c
    print(disp)
    
eur_json.close()