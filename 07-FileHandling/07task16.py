#16.	Write a program that calculates the number of lines for any text file. The user enters the name of the file from the keyboard. Display the result of the calculation (the file name and the number of lines). Do not display the contents of the file. Sample result:
#File name: countries.txt
#Number of lines: 14

file_name = input("Enter file name: ")
lines = 0
with open(file_name) as file:
    for line in file:
        lines += 1
print(f"Number of lines in text: {lines}")