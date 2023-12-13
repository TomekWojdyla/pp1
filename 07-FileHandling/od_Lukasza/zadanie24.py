import csv as csV

plik = "studentslist.txt"
f = open(plik,'r')
content = csV.DictReader(f)

for row in content:
    if int(row['age']) < 30:
        print(f"{row['first_name']} {row['last_name']} {row['email']}")