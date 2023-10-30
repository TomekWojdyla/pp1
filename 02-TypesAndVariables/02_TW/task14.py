#Calculation of circle area and circumference
radius_input = input("Provide circle radius in cm: ")
radius = int(radius_input)
pi = 3.14
#calculate area
circle_area = pi*radius**2
#calculate circumference
circle_circumference = 2*pi*radius
#display results
print(f"For a circle with radius {radius} cm, its circumference equals {circle_circumference} cm and its area equals {circle_area} cm2")