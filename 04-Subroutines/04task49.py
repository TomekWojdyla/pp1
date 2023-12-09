# 49.	The sequence of digits contains the number of points rolled with a dice. Define a function f(dice) that returns a number specifying the number of dice rolled the most times in a row. Sample result:
#f("5233165554211") returns 5
#f("2133") returns 3

def dice_rolls(x):
    y = len(x)
    max_grt = 0
    grt = 0
    for i in range(0,y-1):
        if x[i] == x[i+1]:
            grt = grt+1
            if grt < max_grt:
                pass
            else:
                final = x[i]
                max_grt = grt
        else:
            grt = 0
            pass
    return final


g = dice_rolls("5233165554211")
print(g)
g = dice_rolls("2133")
print(g)