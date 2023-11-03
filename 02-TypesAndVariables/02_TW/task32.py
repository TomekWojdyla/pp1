#32.	23% VAT was paid from an amount. Write a program that reads an amount from the keyboard. Then, it calculates and displays both the amount and its VAT. Apply formatting with two decimal places. Sample result:
#Amount  : 15.84
#VAT 23% :  3.64

import math

amount_str = input("Enter the net. amount value: ")
amount = float(amount_str)
amount_r = round(amount,2)
vat23 = 0.23*amount
vat23_r = round(vat23,2)
vat23_floor = math.ceil(vat23*100/100)
print("Net amount: ", amount)
print("Net amount: ", amount_r)
print("Applied 23% VAT: ", vat23)
print("Applied 23% VAT: ", vat23_r)
print("Applied 23% VAT: ", vat23_floor)

#troche niedoskonałe - zaokrąglanie czasem obcina, precyzja nie jest do drugiego miejsca tylko maksymalnie do 2 miejsca