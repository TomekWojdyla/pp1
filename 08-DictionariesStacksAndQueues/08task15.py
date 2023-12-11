# 15.	The program contains two dictionaries with personal data:
#basic_data = {
#    "name":"Barbara",
##    "age":21
#}

#advanced_data = {
#    "status":"student",
#    "married":False,
#    "interest":["reading","swimming"]
#}
#Write a program that creates a dictionary called ‘person’ containing data from the two given dictionaries (five key-value pairs). Display the contents of the ‘person’ dictionary.

basic_data = {
    "name":"Barbara",
    "age":21
}

advanced_data = {
    "status":"student",
    "married":False,
    "interest":["reading","swimming"]
}

dictionary = {}

for key,value in basic_data.items():
    dictionary.update({(key):(value)})

for key,value in advanced_data.items():
    dictionary.update({(key):(value)})

import json
    
with open("dictionary_test.json","w") as file:
#    json.dump(dictionary,file)
    ttt = json.dumps(dictionary,indent=4)
    file.write(ttt)

print(dictionary)
