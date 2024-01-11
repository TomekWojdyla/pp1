class contact():
    def __init__(self,name,email,mobile):
        self.name = name
        self.email = email
        self.mobile = mobile
    def display_contact(self):
        print(f"{self.name}     {self.email}     {self.mobile}")