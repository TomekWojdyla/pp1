# 29.	Each programming language provides a set of functions that you can use in your programs. One of them is a function that returns a random number. Write a program that displays results of three dice rolls and the sum of dice rolled. Apply a random number generator:
# https://docs.python.org/3/library/random.html 
import random

a = random.randrange(1,7,1)
b = random.randrange(1,7,1)
c = random.randrange(1,7,1)

print(f"First dice throw is {a}")
print(f"Second dice throw is {b}")
print(f"Second dice throw is {c}")

sum = a+b+c

print(f"Sum of the three throws is {sum} ")