#14.	In the TV class, add the channels attribute containing a list of available TV channel names (array). Initially, the array should be empty (TV not programmed, no available channels). Add set_channels(channels_list) and show_channels() methods in the TV class, which allows you to set channels on the TV and display the list of available channels. Sample list of available channels:
#Channel list:
#1. TVP1
#2. TVP2
#. Polsat
#. TVN
#5. Filmbox
#6. Discovery
#Then, try using the TV set:
#a.	Create a TV set
#b.	Show TV status
#c.	Turn TV on
#d.	Show TV status
#e.	Display the list of available channels
#f.	Set TV channels: TVP1, TVP2, Polsat, TVN, Filmbox, Discovery
#g.	Display the list of available channels
#h.	Show TV status
#i.	Turn TV offs

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
            print(f"TV is ON, channel {self.channel_no} - {self.channel_list[self.channel_no]}")
        else:
            print("TV is OFF")
    def set_channel(self):
        kanal = input("Enter new channel no: ")
        self.channel_no = kanal
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
tele.show_channels()
tele.show_status()
tele.turn_off()