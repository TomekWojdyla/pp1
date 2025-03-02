#20.	The bank account has a 26-digit number assigned when creating an account. The initial account balance is PLN 0. You can deposit any amount on the account. You can also withdraw any amount from the account, provided that it does not exceed the account balance. If you try to withdraw a larger amount, the following message will be displayed: "Insufficient funds on the account". At any time, it is possible to display information about the number and balance of the bank account in the following format:
#Bank Account No: 11 1111 1111 1111 1111 1111 1111
#Balance: PLN 25,38
#Create a program that handles the bank account.
#a.	Familiarises yourself with a problem.
#b.	Identify an object
#c.	Define the states and behaviors of the object.
#d.	Transform the states and behaviors of the object into the fields and methods of the class that will serve as a pattern for creating an object.
#e.	Create a sketch of the class without creating any method content.
#f.	Create the content of each method.
#Then, use the program and:
#g.	Create a bank account with the number 12 3456 5555 9090 1111 0000 7722
#h.	Display account balance
#i.	Deposit PLN 25,30
#j.	Display account balance
#k.	Withdraw PLN 31,70
#l.	Display account balance
#m.	Withdraw PLN 14
#n.	Display account balance

class bank_account():
    def __init__(self, number):
        self.accountno = number
        self.balance = 0.00
    def __str__(self):
        return "Bank Account No: " +self.accountno + "\n" + "Balance: PLN " + str(self.balance)
    def deposit(self):
        dep = float(input("Provide the deposit amount: "))
        self.balance +=round(dep,2)
    def withdraw(self):
        withdr = float(input("Provite the withdraw amount: "))
        if withdr>self.balance:
            print("Insufficient funds on the account")
        else:
            self.balance -=withdr


Myaccount = bank_account("12 3456 5555 9090 1111 0000 7722")
print(Myaccount)
Myaccount.deposit()
print(Myaccount)
Myaccount.withdraw()
print(Myaccount)
Myaccount.withdraw()
print(Myaccount)