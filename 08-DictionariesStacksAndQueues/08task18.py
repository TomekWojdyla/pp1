#18.	Create a program that writes to a file ICAO.txt the contents of a dictionary containing ICAO spelling alphabet. Sample file content:
#A Alfa
#B Bravo
#C Charlie
#D Delta
#…
#…
#Z Zulu


import json

icao = open("ICAO.json")
icao_content = json.load(icao)
lent_icao = len(icao_content)
#print(icao_content)

new_file = open("ICAO_NEW.txt","w")

for key, value in icao_content.items():
    a = key
    b = value
    new_file.write(a + " " + b + "\n")


icao.close()
new_file.close()


