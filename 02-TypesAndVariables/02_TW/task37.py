#37.	In Python, to read a range of characters from the string, a slicing method can be used.
#https://www.w3schools.com/python/python_strings_slicing.asp 
#The employee file contains the employee's data in a descriptive form. Write a program in which the personal_data variable contains employee data:
#"Mr. John May, born on 1998-02-16"
#Display the employee's name, surname, initials and date of birth on separate lines. Sample result:
#Description: Mr. John May, born on 1998-02-16
#Name: John
#Surname: May
#Initials: JM
#Born: 1998-02-16

description = "Mr. John May, born on 1998-02-16"
name = description[4:8]
print("Name: ", name)
surname = description[9:12]
print("Surname: ", surname)
initials = description[4:5] + description[9:10]
print("Initials: ", initials)
born = description[22:]
print("Born: ", born)