#13.	In a beverage factory, a machine fills bottles of various capacities. A computer checks whether a bottle has been filled correctly. The allowable tolerance is 2% for a 500ml bottle, 3% for a 1000ml bottle and 5% for a 1500ml bottle. Write a program that checks whether the bottle has been filled correctly or not. Define a higher order function. Sample result:
#507: True
#489: False
#984: True
#1032: False
#1578: False
#1430: True 

import math

def bottle(size):
    def check(vol):
        if size==500:
            if math.fabs(size-vol)<=size*0.02:
                return True
            else:
                return False
        if size==1000:
            if math.fabs(size-vol)<=size*0.03:
                return True
            else:
                return False
        if size==1500:
            if math.fabs(size-vol)<=size*0.05:
                return True
            else:
                return False
    return check

small_bottle = bottle(500)
med_bottle = bottle(1000)
big_bottle = bottle(1500)

a=507
b = small_bottle(a)
print(f"{a}: {b}")

a=489
b = small_bottle(a)
print(f"{a}: {b}")

a=984
b = med_bottle(a)
print(f"{a}: {b}")

a=1032
b = med_bottle(a)
print(f"{a}: {b}")

a=1578
b = big_bottle(a)
print(f"{a}: {b}")

a=1430
b = big_bottle(a)
print(f"{a}: {b}")