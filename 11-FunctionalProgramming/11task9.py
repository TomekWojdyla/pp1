#9.	Write a program that converts speed in meters per second to speed in kilometers per hour. Use an anonymous function. Sample result:
#10 m/s = 36 km/h
#35 m/s = 126 km/h

a=10
c=35
transform = lambda x: x*3.6
b=int(transform(a))
d=int(transform(c))
print(f"{a} m/s = {b} km/h")
print(f"{c} m/s = {d} km/h")