#(p1.py) The vending machine accepts 1, 2 and 5 PLN coins. Define the function f(amount_to_pay) that returns the minimum number of coins that can be used to pay for the purchased product. Sample result:
#f(23) returns 6
#f(8) returns 3

def f(amount_to_pay):
    coins = 0
    con5 = amount_to_pay//5
    con2 = (amount_to_pay-con5*5)//2
    con1 = amount_to_pay-con5*5 - con2*2
    coins = con5+con2+con1
    return coins
    
a = f(8)
print(a)