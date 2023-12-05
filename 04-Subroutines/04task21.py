# 21.	In the module mymath.py, define the function generate_number() that creates and returns random integer number in the range of <1,9>. Then create a main program, in which, first import modules mymath.py and mykeyboard.py, you created earlier. The program is a simple guessing game. The user enters a one-digit number from the keyboard. The computer then generates a random one-digit number. If the numbers match, the user wins the game. Sample result:
#Enter a number: 7
#Computer number: 7
#You won the game!!

import mykeyboard_tw
import mymath_tw

m=mykeyboard_tw.read_number()
n=mymath_tw.generate_number()

print(f"You chose: {m}")
print(f"Computer chose: {n}")
if m==n:
    print("You Won!")
else:
    print("You lost!")
    
