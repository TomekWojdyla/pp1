#10.	Write a program that calculates the average speed of a vehicle. Enter from the keyboard: a distance in km, a number of travel hours and a number of travel minutes. Define a function avg_speed(distance,hours,minutes) that returns the calculated average speed. Sample result:
#Enter distance in km: 70
#Enter number of travel hours: 1
#Enter number of travel minutes: 23
#Average speed: 50.6 km/h 


dist = int(input("Enter disctance in km: "))
hours = int(input("Enter number of travel hours: "))
minutes= int(input("Enter number of travel minutes: "))

def avg_speed(x,y,z):
    time_h = y + z/60
    avg = x/time_h
    return avg

calc = round(avg_speed(dist,hours,minutes),1)
print(f"Avarage speed: {calc} km/h")