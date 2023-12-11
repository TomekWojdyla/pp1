#12.	Write a program in which you create a dictionary containing student data. Try to describe a student in detail, using different data types that can be used in the dictionary. Then, save the data about student in the file student.json, in a readable form.

students = {
    "name": "Tomasz",
    "surname": "Wojdyla",
    "born-place": "Rabka",
    "born-date": 1982,
    "AZS": True,
    "high_school": "Goszczyński Nowy Targ",
    "hobby":["volleyball, snowboard, Python"],
    "telephone":{"work": "126789999","Mobile":"603510248"},
    "email":{"private":"tomiwojdyla@o2.pl", "School":"234216@student.uek.krakow.pl"},
}

import json
with open("student_data.json","a") as task12:
    jsonobject = json.dumps(students, indent=4)
    print(jsonobject)
    task12.write(jsonobject)