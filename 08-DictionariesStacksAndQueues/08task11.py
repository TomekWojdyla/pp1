#11.	Create a dictionary that describes your favorite book or movie with at least five key-value pairs. Then, create a program that writes the dictionary data to the favourite.json file. Use the dump() method. Pay attention to the formatting of the data in the json file. Use the 'indent' parameter in the dump() method. Sample result:
#movie = {
#    "title":"…",
#    "year": …,
#    "actor":{"leading":"…","supporting":"…"},
#    "oscar":False,
##    …
#    …
#    …
#}

movie = {
    "title":"Everest",
    "year": 2015,
    "director": "Baltasar Kormákur",
    "length": "140min",
    "actors":["Jason Clarke","Jake Gyllenhaal", "Emily Watson"],
}

import json

data_movie = open("favourite.json","w")
json_object = json.dumps(movie, indent=4)
data_movie.write(json_object)
data_movie.close()

with open("favourite.json") as sample:
    k = json.load(sample)

i=0
#while i<len(k):
print(k["title"],k["length"])
#    i+=1