#11.	Write a program that calculates the average speed of a vehicle. Enter from the keyboard: a distance in km, a number of travel hours and a number of travel minutes. Use an anonymous function. Sample result:
#Enter distance in km: 70
#Enter number of travel hours: 1
#Enter number of travel minutes: 23
#Average speed: 50.6 km/h 

dist = int(input("Enter disctance in km: "))
hours = int(input("Enter number of travel hours: "))
minutes= int(input("Enter number of travel minutes: "))
avg_speed = lambda x,y,z: round(x/(y+z/60),1)
calc = avg_speed(dist,hours,minutes)
print(f"Avarage speed: {calc} km/h")