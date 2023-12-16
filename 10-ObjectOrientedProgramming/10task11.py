#11.	Write a program in which create a TV class that describes a TV set. The class should contain one boolean attribute called 'is_on' that specifies whether the TV set is turned on. Initially, the TV is turned off. Add turn_on() and turn_off() methods in the class to turn the TV on and off, respectively. Also, add a show_status() method to display whether the TV is on or off. Sample message:

#a.	Create TV set
#b.	Show TV status
#c.	Turn TV on
#d.	Show TV status
#e.	Turn TV off
#f.	Show TV status


class TV():
    def __init__(self):
        self.is_on = False
    def turn_off(self):
        self.is_on = False
    def turn_on(self):
        self.is_on = True
    def show_status(self):
        if self.is_on==True:
            print("TV is ON")
        else:
            print("TV is OFF")

telewizor = TV()
telewizor.show_status()
telewizor.turn_on()
telewizor.show_status()
telewizor.turn_off()
telewizor.show_status()
