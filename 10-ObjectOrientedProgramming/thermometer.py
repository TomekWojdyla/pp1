import random

class therm():
    def __init__(self):
        self.is_on = False
        self.therm_indication = 0
    def turn_on(self):
        self.is_on = True
    def turn_off(self):
        self.is_on = False
    def measure(self):
        temp = random.randint(34,41) + round(random.random(),1)
        msg = "Temperature: " + str(temp)+"C"
        if temp >= 37 and temp <41:
            msg += " (fever)"
            print(msg)
        elif temp>=41:
            msg += " \"CRITICAL TEMPERATURE\""
            print(msg)
        else:
            print(msg)
            
        
