#25.	Measuring stations recorded the following temperatures in degrees Celsius:
#{"Krakow":7,"Warszawa":-2,"Sopot":4,"Koszalin":-1,"Opole":3}
#Write a program that displays the names of towns where positive temperatures were recorded. Use anonymous and filter() functions. Sample result:
#	Cities with positive temperatures: Krakow Sopot Opole


temp = {"Krakow":7,"Warszawa":-2,"Sopot":4,"Koszalin":-1,"Opole":3}
a = temp["Krakow"]
print(a)
a = []
for key,value in temp.items():
    if value>0:
        a.append(key)
    else:
        pass
print(a)


#nie wiem

temp = {"Krakow":7,"Warszawa":-2,"Sopot":4,"Koszalin":-1,"Opole":3}
new = dict(filter(lambda x: x[1]>0, temp.items()))
new1 = list(map(lambda x: x[0],new.items()))
print(new)
print(new1)

