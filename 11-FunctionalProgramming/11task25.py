#25.	Measuring stations recorded the following temperatures in degrees Celsius:
#{"Krakow":7,"Warszawa":-2,"Sopot":4,"Koszalin":-1,"Opole":3}
#Write a program that displays the names of towns where positive temperatures were recorded. Use anonymous and filter() functions. Sample result:
#	Cities with positive temperatures: Krakow Sopot Opole


temp = {"Krakow":7,"Warszawa":-2,"Sopot":4,"Koszalin":-1,"Opole":3}
a = temp["Krakow"]
print(a)
temp_check = list(filter(lambda x: x[key]>0,temp))
    
print(temp_check)


#nie wiem