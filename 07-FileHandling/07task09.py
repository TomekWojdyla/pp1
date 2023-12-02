#9.	Create a program that displays the contents of the countries.txt text file. At the beginning of each line, display the line number. Tip: read and display text file line by line. Sample result:
# open file
#...

# display text file, line by line
#counter = 0
#for line in file:
#    counter += 1
#     print(f"{counter}. {line}", end="")

# close file
#... 
#1. Poland
#2. Germany
#3. Slovakia
#4. Ukraine
#5. Lithuania

#open file
file = open("countries_tw.txt")
#counter
number =0
#read by line
for line in file:
#alt  line = line.rstrip()
    number +=1
#alt  print(f"{number}. {line}")
    print(f"{number}. {line}", end="")
print()
file.close()
    