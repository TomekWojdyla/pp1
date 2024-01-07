#16.	Create a class that describes cell phones with at least 3 phone states and 2 behaviors. Define a text representation of an object. Then, create 2 objects. Display their features and call their bahaviors.

class mobile():
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.is_on = False
        self.volume = 0
    def __str__(self):
        return "My super phone is " + self.brand +" " + self.model + " vol level: "+str(self.volume)
    def volume_up(self):
        self.volume +=1
    def volume_down(self):
        self.volume -=1
        
MyCell = mobile("Samsung","A71", 2021)
HerCell = mobile("Xiaomi","Redmi Note", 2022)

print(MyCell)
MyCell.volume_up()
MyCell.volume_up()
print(MyCell)
print(HerCell)
HerCell.volume_up()
HerCell.volume_up()
HerCell.volume_down()
print(HerCell)