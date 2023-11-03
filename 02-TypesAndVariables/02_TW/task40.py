#40.	The credit card number consists of 16 digits. Write a program that allows you to enter a credit card number from the keyboard. Display the credit card number in groups of 4 digits, separating the groups with a space character. Sample result:
#Enter credit card number: 5020312109004442
#Card number: 5020 3121 0900 4442

card_no = input("Enter credit card number (no spaces and special signs): ")
card_no_f = card_no[:4]+" "+card_no[4:8]+" "+card_no[8:12]+" "+card_no[12:]
print("Formated Card number: ", card_no_f)