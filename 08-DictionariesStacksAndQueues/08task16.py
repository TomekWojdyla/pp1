#16.	A program contains two functions:
#a.	hotel_list(hotels) that returns a list of hotels names, separated by a comma sign
#b.	avg_price(hotels) that returns the average room price for a given list of hotels, rounded to an integer value
##c.	
#Write a program that calculates and displays the average price for a room in hotels in Krakow and Sopot and indicates in which cities hotels are cheaper.
#Hotels_in_Krakow = [
#    {"name":"Sky","price":320.00},
#    {"name":"Metropol","price":480.00},
#    {"name":"New Port","price":420.00},
#    {"name":"Aparthotel","price":390.00}
#]
#hotels_in_Sopot = [
#    {"name":"Focus","price":510.00},
#    {"name":"Aqua","price":345.00},
#    {"name":"La Boutique","price":390.00},
#    {"name":"Marina","price":410.00}
#]
#Sample result:
#Hotels in Krakow: …,…,…,…
#Average hotel price in Krakow: …
#Hotels in Sopot: …,…,…,…
#Average hotel price in Sopot: …
#Cheaper hotels in: …

Hotels_in_Krakow = [
    {"name":"Sky","price":320.00},
    {"name":"Metropol","price":480.00},
    {"name":"New Port","price":420.00},
    {"name":"Aparthotel","price":390.00}
]
hotels_in_Sopot = [
    {"name":"Focus","price":510.00},
    {"name":"Aqua","price":345.00},
    {"name":"La Boutique","price":390.00},
    {"name":"Marina","price":410.00}
]

def hotel_list(hotels):
    lent = len(hotels)
    disp = ""
    for i in range(lent):
        g = hotels[i]["name"]
        disp += g + ","
    return disp

def avg_price(hotels):
    lent = len(hotels)
    sum = 0
    for i in range(lent):
        g = hotels[i]["price"]
        sum += g
    avg = round(sum/lent)
    return avg

g = hotel_list(Hotels_in_Krakow)
print(f"Hotels in Krakow: {g}")

h = avg_price(Hotels_in_Krakow)
print(f"Avarage hotel price in Krakow is: {h}")

k = hotel_list(hotels_in_Sopot)
print(f"Hotels in Sopot: {k}")

l = avg_price(hotels_in_Sopot)
print(f"Avarage hotel price in Sopot is: {l}")

if h<l:
    print("Hotels are cheaper in Krakow")
else:
    print("Hotels are cheaper in Sopot")