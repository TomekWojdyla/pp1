#15.	In the TV class, make changes to the show_status() method so that it displays not only the selected channel number but also its name. When the selected channel number exceeds the list of available channels, the channel name is not displayed.
#TV is on, channel 4 (TVN)
#Then, try using the TV. Set at least 7 channels (seven TV stations), change channel numbers and display TV status every time.

class TV():
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        self.channel_list = []
    def turn_on(self):
        self.is_on = True
    def turn_off(self):
        self.is_on = False
    def show_status(self):
        if self.is_on == True:
            print(f"TV is ON, channel {self.channel_no} ({self.channel_list[self.channel_no-1]})")
        else:
            print("TV is OFF")
    def set_channel(self):
        kanal_enter = False
        while kanal_enter == False:
            kanal = int(input("Enter new channel no: "))
            if kanal<= len(self.channel_list)+1:
                self.channel_no = kanal
                kanal_enter = True
            else:
                print("Not a number try again: ")
    def set_channels(self):
        enter = False
        while enter==False:
            new_channel = input("Add new channel name or hit enter to exit: ")
            if new_channel != "":
                self.channel_list.append(new_channel)
            else:
                enter = True
    def show_channels(self):
        desc = "Channel list:"
        for i in range(len(self.channel_list)):
            desc += "\n"+str(i+1)+". " + self.channel_list[i]
        print(desc)
    def __str__(self):
        return "Moj televizor Szajsung"


tele = TV()

tele.show_status()
tele.turn_on()
tele.show_channels()
tele.set_channels()
tele.show_status()
tele.set_channel()
tele.show_status()
tele.set_channel()
tele.show_status()
tele.set_channel()
tele.show_status()
tele.set_channel()
tele.show_status()
tele.set_channel()
tele.show_status()
tele.set_channel()
tele.show_status()
tele.turn_off()
tele.show_status()