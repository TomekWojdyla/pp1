#20.	In the module mykeyboard.py, define a function read_number() that returns an integer number entered from the keyboard. The function should print a text prompting user to enter data 'Enter a number: '. Then, use the function to read two numbers from the keyboard. To test the function, use the __name__ variable. Display the sum of two entered numbers. Sample result:
#Enter a number: 34
#Enter a number: 7
#34 + 7 = 41

import mykeyboard_tw

n=mykeyboard_tw.read_number()
m=mykeyboard_tw.read_number()
c=n+m

print(f"{n} + {m} = {c}")