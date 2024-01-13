import contact as co

class contact_list():
    def __init__(self):
        self.contacts =[]
    def add_contact_to_list(self):
        new_contact = {}
        new_name = input("Enter a contact name: ")
        new_email = input("Enter a contacts email: ")
        new_mobile = input("Enter a contact mobile: ")
        new_contact = co.contact(new_name,new_email,new_mobile)
#        new_contact = {"name":new_name,"email":new_email,"mobile":new_mobile}
        self.contacts.append(new_contact)
    def __str__(self):
        listed = "test print"
        return listed
    def show_list(self):
        for i in range(len(self.contacts)):
            record = self.contacts[i]
            record.co
    

test_list = contact_list()
print(test_list)
test_list.add_contact_to_list()
test_list.show_list()