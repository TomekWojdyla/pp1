#area and circumference of triangle from input
a_string = input("Enter the lenght of first triangle side 'a': ")
a = int(a_string)
b_string = input("Enter the lenght of first triangle side 'b': ")
b = int(b_string)
c_string = input("Enter the lenght of first triangle side 'c': ")
c = int(c_string)
#area from Heron formula
p = 0.5*(a+b+c)
area = (p*(p-a)*(p-b)*(p-c))**0.5
print("Triangle area equals to: ", area)
#circumference
circ = a + b + c
print("Triangle circumference equals to: ", circ)