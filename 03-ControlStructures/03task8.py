#8.	The speed limit on a motorway in Poland is 140 km/h. Write a program that checks whether a car exceeded the speed limit. If so, a warning is displayed. Sample 

print("Speed limit in polish motorway is 140km/h")
speed_str = input("Enter your car speed in km/h: ")
try:
    speed = float(speed_str)
    if speed>= 140:
        print("Warning: speed limit exceeped!! Slow down!!")
    else:
        print("You're moving like a tuttle... ;)")
except:
    print("what have you eneteren? was tha a number?")