#24.	An object contains a list of coordinates of points on the plane, as a two-dimensional array. Define a C class that allows you to create an object. Provide the list of coordinates of points at the time of creating the object. In the class C, define a method m(n) that returns true when at least n points are in the first quadrant of the coordinate system (both point coordinates are greater than 0), or false otherwise. Sample result:
#C([[2,3],[1,8],[-6,4],[3,-7]])
#m(2) returns True
#m(3) returns False

class C():
    def __init__(self,coord):
        self.points = coord
    def m(self, limit):
        count = len(self.points)
        firstq_count = 0
        for i in range(count):
            if self.points[i][0]>0 and self.points[i][1]>0:
                firstq_count +=1
            else:
                pass
        if firstq_count >= limit:
            output = True
        else:
            output = False
        return output

test = C([[2,3],[1,8],[-6,4],[3,-7]])
a = test.m(2)
print(a)
b = test.m(3)
print(b)