#24.	In a separate module, define a function that checks if the number is within the range <x, y>. The function returns a boolean value. Then, create a program and use the function you defined. Sample result:
#A number: 7
#umber 7 in the range <2,15>: yes 


import number_in_range

no1 = int(input("Enter begining of range: "))
no2 = int(input("Enter end of range: "))
no3 = int(input("Enter number to check: "))

check = number_in_range.num_in_range(no3, no1, no2)
print(f"Number {no3} is within range <{no1},{no2}>: {check}")
