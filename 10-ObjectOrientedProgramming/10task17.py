#17.	In the TV class, add support for volume adjustment in the range 0 to 10. The initial value of the volume level is 0. Add two methods to increase and decrease the TV volume level by one. Note that you cannot increase or decrease the volume beyond the specified range. Display the current volume level in the show_status() method. Then check the operation of the TV by adjusting and displaying its volume level.


class TV():
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        self.channel_list = []
        self.volume = 0
    def turn_on(self):
        self.is_on = True
    def turn_off(self):
        self.is_on = False
    def show_status(self):
        if self.is_on == True:
            print(f"TV is ON, channel {self.channel_no} ({self.channel_list[self.channel_no-1]} and volume is {self.volume})")
        else:
            print("TV is OFF")
    def volume_up(self):
        if self.volume < 10:
            self.volume += 1
        else:
            print(f"TV is at max volume: {self.volume}")
    def volume_down(self):
        if self.volume > 0:
            self.volume -= 1
        else:
            print(f"TV is at min volume: {self.volume}")
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
tele.volume_up()
tele.volume_up()
tele.volume_up()
tele.volume_up()
tele.volume_up()
tele.show_status()
tele.volume_up()
tele.volume_up()
tele.volume_up()
tele.volume_up()
tele.volume_up()
tele.volume_up()
tele.volume_up()
tele.volume_up()
tele.show_status()
tele.volume_down()
tele.volume_down()
tele.volume_down()
tele.volume_down()
tele.volume_down()
tele.show_status()
tele.volume_down()
tele.volume_down()
tele.volume_down()
tele.volume_down()
tele.volume_down()
tele.volume_down()
tele.volume_down()
tele.turn_on()
tele.show_status()