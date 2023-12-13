# 29.	The grades.txt file contains student’s grades. Create the file in any text editor with the content as below:
#Name: Peter
#Grades: 3.5, 4.0, 5.0, 4.5, 3.5, 3.0, 5.0
#Then, create a program that calculates the arithmetic mean of student’s grades.

import re

file1 = open("grades.txt")
file_content = file1.read()
#print(file_content)

grades = re.findall(r"\b\d.\d\b",file_content)
print(grades)

sum = 0
for i in range(len(grades)):
    sum+= float(grades[i])

avg = sum/len(grades)
print(avg)