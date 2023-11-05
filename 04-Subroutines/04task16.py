#16.	Define a function product(x, y) that displays a product of two numbers. Then, call the function.
#def product(x,y):
#    return x*y

#a = 3
#b = 4
#print(f"The product of {a} and {b} is {product(a,b)}")

def product (x,y):
    return x*y

a=float(input("Enter number a: "))
b=float(input("Enter number b: "))

#pro = product(a,b)
#print(f"The product of {a} and {b} equals {pro}")
print(f"The product of {a} and {b} equals {product(a,b)}")