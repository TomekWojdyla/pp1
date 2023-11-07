#22.	Most female names in Polish end with the letter "a". Write a program that displays the name entered from the keyboard, provided it is a female name. Sample result:

name = input("Enter name: ")
b=name[-1]
print(b)
if b=="a":
    print(f"{name} is a Polish female name.")
else:
    print(f"{name} is a Polish male name.")