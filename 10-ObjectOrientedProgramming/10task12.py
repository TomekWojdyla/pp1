#12.	In the TV class, add the channel_no attribute indicating the number of the TV channel displayed by the TV set. Initially, the TV is set to channel 1. Modify the show_status() method so that it also displays the TV channel number, but only if the TV is turned on:
#TV is on, channel 1
#Then, try using the TV set.

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
    def __str__(self):
        return "Moj televizor Szajsung"
            
telewizor = TV()
print(telewizor)
telewizor.show_status()
telewizor.turn_on()
telewizor.show_status()
telewizor.turn_off()
telewizor.show_status()

