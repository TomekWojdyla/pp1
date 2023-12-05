#23.	Create a program that calculates how many times the given letter appears in any text. Then create a program and check how many times the letter ‘e’ appears in the text below. In a separate module, define a function for making calculations. Sample result:
#You never get a second chance to make a first impression
#The number of letter 'e': 7

import check_letter_tw

text_to_check = input("Enter text: ")
letter = input("Enter letter to check: ")

control = check_letter_tw.check_letter(letter, text_to_check)

print(f"The count of {letter} in provided test is: {control}")


