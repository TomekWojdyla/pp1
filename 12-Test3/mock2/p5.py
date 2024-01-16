#(p5.py) Class C describes a point (x,y) in the plane. The point coordinates are given when creating (initializing) the object. The class contains the m1() method that returns the number of the quadrant of the Cartesian system in which the point (x,y) is located ( https://en.wikipedia.org/wiki/Quadrant_(plane_geometry) ). The m1() method returns 0 if the point (x,y) is located on the X-axis or Y-axis. The class contains the m2(a,b) method that returns true when the point (x,y) is in the same quadrant of the Cartesian system as the point with coordinates a,b. Otherwise, the method returns false. The class contains the m3(a,b) method that returns true when the distance between points (x,y) and (a,b) is greater than 5. Otherwise, the method returns false. Example:
#p = C(2,3)
#p.m1()  1
#p.m2(7,4)  True
#p.m2(-3,1)  False
#p.m3(8,5)  True
#p.m3(4,7)  False
#p1 = C(0,5)
#p1.m1()  0
#p1.m2(4,7)  False
#p1.m2(-7,0)  True

class C():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def m1(self):
        if self.x==0 or self.y==0:
            return 0
        elif self.x>0 and self.y>0:
            return 1
        elif self.x<0 and self.y>0:
            return 2
        elif self.x<0 and self.y<0:
            return 3
        else: 
            return 4
    def m2(self,a,b):
        if (self.x>0 and a>0) or (self.x<0 and a<0):
            if (self.y>0 and b>0) or (self.b<0 and b<0):
                return True
            else:
                return False
        else:
            return False
    def m3(self,a,b):
        dist = ((self.x-a)**2 + (self.y-b)**2)**0.5
        if dist>5:
            return True
        else:
            return False

p = C(2,3)
a = p.m1()
print(a)
a = p.m2(7,4)
print(a)
a = p.m2(-3,1)
print(a)
a = p.m3(8,5)
print(a)
a = p.m3(4,7)
print(a)
p = C(0,5)
a = p.m1()
print(a)
a = p.m2(4,7)
print(a)
a = p.m3(-7,0) #typo w przykładzie?? pisało p.m2(-7,0) -> True co jest raczej nie OK
print(a)
