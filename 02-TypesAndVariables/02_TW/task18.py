x = 7
y = 34
print(f"original values: x={x}, y={y}")
#zmienna pomocnicza
aux = x
x = y
y = aux
print(f"variables after swapping: x={x}, y={y}")

x = 6
y = 31
print(f"original values: x={x}, y={y}")
#bez zmiennej pomocniczej
x=x+y
y=x-y
x=x-y
print(f"variables after swapping: x={x}, y={y}")

x = 5
y = 25
print(f"original values: x={x}, y={y}")
#bez zmiennej pomocniczej
x,y = y,x
print(f"variables after swapping: x={x}, y={y}")