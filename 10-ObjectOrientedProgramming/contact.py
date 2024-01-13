class contact():
    def __init__(self,name,email,mobile):
        self.name = name
        self.email = email
        self.mobile = mobile
        self.full_contact = {"name":self.name,"email":self.email,"mobile":self.mobile}
    def display_contact(self):
        print(f"{self.name}     {self.email}     {self.mobile}")
    def __str__(self):
        return self.name+"    "+self.email+"    "+self.mobile
        

#test = contact("John Brown","brown@onet.pl","555234000")
#print(test)