#(p5.py) A counter allows you to count any elements. Define a class C to create counters. The initial value of the counter is assigned when the object is created. The class contains the following methods:
#•	m1() - returns the counter value
#•	m2() - increases the counter value by 1
#•	m3() - decreases the counter value by 1
#•	m4(n) - increases/decreases the counter value by n
#•	__str__ - returns a string representation of the counter value
#Example:
#c=C(5)
#c.m1()  5
#c.m2()
#c.m1()  6
#c.m4(-8)
#c.m1()  -2
#c.m3()
#c.m1()  -3
#c.m4(10)
#c.m1()  7
#c.__str__()  "7"


class C():
    def __init__(self,counter):
        self.counter = counter
    def m1(self):
        return self.counter
    def m2(self):
        self.counter +=1
    def m3(self):
        self.counter -=1
    def m4(self,n):
        self.counter = self.counter+n
    def __str__(self):
        return str(self.counter)
    
    
c = C(5)
c.m1()
c.m2()
c.m1()
c.m4(-8)
c.m1()
c.m3()
c.m1()
c.m4(10)
c.m1()
print(c)