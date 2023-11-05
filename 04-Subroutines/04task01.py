#1.	Subroutines, and specifically functions, are a convenient way to divide a program code into useful blocks, allowing to make a program code more readable, reuse it and save some time. A function is a block of code which only runs when it is called. There are a number of built-in functions, ready to use, e.g. len(), print(), input() or type().
#https://docs.python.org/3/library/functions.html 
#Using built-in Python functions, write a program that calculates and displays:
#a.	length of the phrase: "computer science"
#b.	letter read from the keyboard
#c.	string representing the number 5068
#d.	numeric representing the string "20303"
#e.	the smallest number given: 4,7,2,3,9,8

length = len("computer science")
print(f"Computer science expresion length is {length} signs.")

letter = input("Enter a letter: ")
print("Great! Your letter is: ",letter)

representation = str(5068)
print(f"Representation of 5068 number is {representation} that is {type(representation)}")

no = 20303
number = str(no)
print(f"{no} is a {type(no)}, but {number} is a {type(number)}")

b=min[4,7,2,3,9,8]
print("Smallest number from given collection 4,7,2,3,9,8 is: ", b)