#31.	Write a program that enables a user to challenge a computer. The computer throws dice. Then, the user then tries to guess the number from dice by entering a number from 1 to 6 from the keyboard. If the user has guessed the number from the dice, the computer displays True. Otherwise, the computer displays False.

import random

a=random.randrange(1,7,1)
b=random.randrange(1,7,1)
guess=input("Try to guess the number on dice. Enter your number: ")
guess=int(guess)
print("Have you guessed?", (guess==a or guess==b))
print(f"My numbers were: {a} and {b}.")

