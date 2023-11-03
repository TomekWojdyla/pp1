#38.	To improve readability, telephone numbers are often presented with a dash or space separating some digits. Write a program that displays a 9-digit telephone number entered from the keyboard as three groups of 3 digits each, separated by a dash character. Sample result:
#Enter phone number: 543097329
#Phone number: 543-097-329

no = input("Enter phone number (9 digits, no spaces and special signs): ")
no_formated = no[:3]+"-"+no[3:6]+"-"+no[6:]
print("Formated phone number: ", no_formated)
