#6.	Familiarise yourself with defining anonymous (lambda) functions in Python.
#https://youtu.be/25ovCm9jKfA?feature=shared 

#7.	Define an anonymous function that calculates the body mass index (BMI) for the given weight in kg and height in cm. Then, calculate the BMI for Peter (81kg, 182cm). Sample result:
#Peter’s BMI is …

#test z video
#g = lambda x: 3*x-1
#data = float(input("podaj x: "))
#print("wynik ",g(data))

#7
h = lambda x, y : x/(y/100)**2
wei = float(input("Podaj wage [kg]: "))
hei = float(input("Podaj wzrost [cm]: "))
BMI = h(wei,hei)
print("policzone BMI wynosi: ",BMI)
print("policzone BMI wynosi: ",f"{BMI:.2f}")
