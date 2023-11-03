#30.	In many games, the numbers one and six on dice have special meaning. Write a program that displays the number of dice rolled and the value True if the number rolled is 1 or 6. Sample result:
#Dice rolled: 4
#Special number: False

import random
a = random.randrange(7)
print(f"Number on the rolled dice: {a}")
print("Is this a special number?",a==1 or a==6)