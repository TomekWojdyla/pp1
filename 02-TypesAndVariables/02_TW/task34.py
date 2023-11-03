# 34.	The speed of vehicles on a highway in Poland must be between 40 and 140 km/h. Write a program that checks whether the vehicle speed entered from the keyboard is correct. Sample result:
#Enter vehicle speed: 158
#Speed is valid: False

speed_str = input("Enter the car speed: ")
#you could add entry validation
speed=float(speed_str)
print("Your speed is acceptable on the highway <40,140> km/h: ", speed>=40 and speed<=140)
