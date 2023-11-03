#32.	23% VAT was paid from an amount. Write a program that reads an amount from the keyboard. Then, it calculates and displays both the amount and its VAT. Apply formatting with two decimal places. Sample result:
#Amount  : 15.84
#VAT 23% :  3.64

import math

amount_str = input("Enter the net. amount value: ")
amount = float(amount_str)
#amount_r = round(amount,2)
amount_r = f"{amount:.2f}" # uwaga zwraca string
vat23 = 0.23*amount
#vat23_r = round(vat23,2) - niedoskonałe, obcina zera
#vat23_floor = math.floor(vat23*100/100) #zwraca integer
vat23_format = f"{vat23:.2f}" #uwaga zwraca string
print("Net amount: ", amount_r)
#print("Applied 23% VAT: ", vat23)
#print("Applied 23% VAT: ", vat23_r)
#print("Applied 23% VAT: ", vat23_floor)
print("Applied 23% VAT: ", vat23_format)

#troche niedoskonałe - zaokrąglanie czasem obcina, precyzja nie jest do drugiego miejsca tylko maksymalnie do 2 miejsca