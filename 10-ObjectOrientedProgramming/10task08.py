#8.	Identify at least 3 states and 3 behaviors for a telephone object. Then, for the listed states and behaviors, create a class with fields (attributes) and methods. Try to use verbs in method names as they describe activities. Finally, create a object, call its methods and display object’s properties.


class Phone():
    def __init__(self,brand,model,size):
        self.brand = brand
        self.model = model
        self.size = size
        self.is_answered = False
        self.is_on = True
        self.last_txt = ""
    def turnoff(self):
        self.is_on = False
    def turnon(self):
        self.is_on = True
    def answer(self):
        self.is_answered = True 
    def end_call(self):
        self.is_answered= False
    def send_txt(self,txt):
        self.last_txt = txt
    
myphone = Phone("Samsung","A72",6)

print(f"My phone is {myphone.brand} {myphone.model}")

myphone.turnoff()
print(f"my phone is on: {myphone.is_on}")

myphone.turnon()
print(f"my phone is on: {myphone.is_on}")

sms= input("Enter text to send: ")
myphone.send_txt(sms)
print(f"Last txt I have sent was: {myphone.last_txt}")