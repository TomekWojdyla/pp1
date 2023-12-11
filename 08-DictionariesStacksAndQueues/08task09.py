#9.	Create an array with 5 dictionaries, each containing a country and its population. Then, using a ‘while’ loop, display the array contents. Sample result:
#countries = [
#    {"name":"Poland", "population":38000000},
#    …
#    …
#    …
#    …
#]
#COUNTRY  POPULATION
#Poland   38000000
#…        …
#…        …
#…        …
#…        …


countries = [
    {"name":"Poland", "population":38000000},
    {"name":"Germany", "population":70000000},
    {"name":"Sweden", "population":5000000},
    {"name":"Monaco", "population":380000},
    {"name":"China", "population":1338000000},
]

i=0
while i < len(countries):
    print(countries[i]["name"], countries[i]["population"])
    i += 1
