#13.	Add the set_channel(new_channel_no) method in the TV class to set the TV channel number. Then try using the TV set.
#a.	Create a TV set
#b.	Show TV status
#c.	Turn TV on
#d.	Show TV status
#e.	Change TV channel to 5
#f.	Show TV status
#g.	Turn TV off
#h.	Show TV status 


class TV():
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
    def turn_on(self):
        self.is_on = True
    def turn_off(self):
        self.is_on = False
    def show_status(self):
        if self.is_on == True:
            print(f"TV is ON, channel {self.channel_no}")
        else:
            print("TV is OFF")
    def set_channel(self):
        kanal = input("Enter new channel no: ")
        self.channel_no = kanal
    def __str__(self):
        return "Moj televizor Szajsung"
            
telewizor = TV()
print(telewizor)
telewizor.show_status()
telewizor.turn_on()
telewizor.show_status()
telewizor.set_channel()
telewizor.show_status()
telewizor.turn_off()
telewizor.show_status()