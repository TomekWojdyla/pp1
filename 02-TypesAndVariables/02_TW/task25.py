#25.	People up to and including 26 years of age are exempt from paying taxes in Poland. Write a program that, based on the person's age entered from the keyboard, displays True if the person is exempt from paying taxes and displays False otherwise
age_string = input("Enter persons age (use natural number only): ")
age = float(age_string)
tax_free = age<=26
print(f"Exemption from paying taxes due to young age: {tax_free}")
