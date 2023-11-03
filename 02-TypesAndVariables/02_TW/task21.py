height_cm_string=input("Enter your height in cm (please use natural number only): ")
height_cm_int= int(height_cm_string)
height_inch = height_cm_int//2.54
print("inches:",height_inch)
height_feet=height_inch//12
height_remaining_inches = height_inch%12
print(f"You are {height_cm_int}cm tall. In imperial system that equals to approximately {height_feet} feet and {height_remaining_inches} inches ({height_feet}'-{height_remaining_inches}).")