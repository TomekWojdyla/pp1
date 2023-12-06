# 36.	A device in a door registers people entering and leaving a room. The + sign means a person entering a room and the – sign a person leaving a room. Define the function f(detector) that returns True if at least 3 people were in the room at the same time, or False otherwise. Sample result:
#f("+-+++-+---") returns True
#f("+-+-+-+-") returns False
#f("+-++-+--") returns False
#f("+-++-++-+---") returns True


def check(a):
    for i in range(0,len(a)):
        if a[i]=="+" and a[i+1]=="+" and a[i+2]=="+":
            disp = True
            break
        elif a[i]=="+" and a[i+1]=="+" and a[i+2]=="-" and a[i+3]=="+" and a[i+4]=="+":
            disp = True
            break
        else:
            disp = False
    return disp

g = check("+-+++-+---")
print(g)
g = check("+-+-+-+-")
print(g)
g = check("+-++-+--")
print(g)
g = check("+-++-++-+---")
print(g)
g = check("++--+++++----++-++++--+-++---")
print(g)