#25.	A stadium is divided into sectors, each marked with a letter. There is a certain number of fans in each sector. Define the class C, which allows you to create an object representing the stadium with a list of sectors and the number of fans in sectors. Data, as a dictionary, should be transferred to the object at the time of its creation. Define in the class a method m1(s,n) that allows you to change the number of fans n in sector s or add a new sector s with the given number of fans n. Define in the class a method m2(s) that returns the sum of fans in the sectors listed in the string s. Sample result:
#C({"A":120,"D":150,"G":90,"K":110})
#m1("G",130)
#m2("GD") returns 280
#m2("KEJ") returns 110

class C():
    def __init__(self, dict):
        self.stadium = dict
    def m1(self, s,n):
        for key in self.stadium:
            if key == s:
                self.stadium[key] = n
            else:
                pass
        return self.stadium
    def m2(self,s):
        leng = len(s)
        sum = 0
        for i in range(leng):
            letter = s[i]
            for key in self.stadium:
                if key==letter:
                    sum +=self.stadium[letter]
        return sum
    
test = C({"A":120,"D":150,"G":90,"K":110})
a = test.m1("G",130)
print(a)
b=test.m2("GD")
print(b)
c=test.m2("KEJ")
print(c)