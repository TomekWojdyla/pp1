#3.	Familiarise yourself with the concept of  dividing the program code into a smaller parts that performs specific tasks.
# https://youtu.be/NE97ylAnrz4?feature=shared 

#4.	From the textbook, read the chapter 4 (Functions). 
#5.	Complete all exercises available in the textbook, chapter 4, Exercise section.


import math

def ping():
   return "PING!"

b = ping()
print("say what?", b)

def volume(r):
    #objetosc kuli
    v = 4.0/3.0*math.pi*r**3
    return v

r_def = float(input("Enter sphere radius: "))
Vol = volume(r_def)
print(f"Sphere volumne with {r_def} radius equals {Vol}")


c = float(input("liczba z przecinkiem"))

d = int(c)
print("liczba int",d)