#33.	The password is valid if it is at least 8 characters long. Write a program that checks whether the password read from the keyboard is correct. Sample result:
#Enter password: qwertyXX
#Password is valid: True

password = input("Enter your password: ")

length=len(password)
check = length>=8
print(f"YOur password contains {length} signs.")
print("Password is valid: ", check)