#25.	Define an anonymous function that returns True when the first number is greater than the second one. Otherwise returns False. Use a conditional operator. Then, check the function for pairs of numbers: 34, 25 and 19,23.

x=19
y=23

if x>y:
    g=lambda x,y: True
    print(g(x,y))
else:
    g=lambda x,y: False
    print(g(x,y))
#annonym = lambda x,y: if x>y: True else: False

