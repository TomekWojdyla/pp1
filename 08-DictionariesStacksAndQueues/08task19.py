#19.	Using the website https://mockaroo.com, generate a list of 500 students, containing the following data: name, surname, student ID, gender, age, year of study, email. Write the data to the students.json file. Then, write a program that creates the limited.json file containing the list of students limited to data: first name, last name, student id.

import json

students_file = open("students.json")
students_content = json.load(students_file)
print(type(students_content))

#print(students_content)
lent = len(students_content)
print(lent)

students_lim = open("limited.json","w")
#students_lim.write("[")

tot = []
for i in range(lent):
    a = students_content[i]["first_name"]
    b = students_content[i]["last_name"]
    c = students_content[i]["student_id"]
    d = {"first_name":a,"last_name":b,"student_id":c}
    tot.append(d)
  
save = json.dumps(tot,indent=4)
students_lim.write(save)
#students_lim.write("]")
students_file.close()
students_lim.close()
