#8.	Write a program that converts speed in meters per second to speed in kilometers per hour. Define a function ms_to_kmh(ms) that returns the calculated speed in km/h. Sample result:
#10 m/s = 36 km/h
#35 m/s = 126 km/h

def ms_to_kmh(speed):
    kmh = (speed*3600)/1000
    return int(kmh)

a = 10
b = ms_to_kmh(a)
print(f"{a} m/s = {b} km/h")

a = 35
b = ms_to_kmh(a)
print(f"{a} m/s = {b} km/h")