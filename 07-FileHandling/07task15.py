#15.	The following program displays the contents of a file, line by line:
#f = open("filename.txt")
#for line in f:
#     print(line, end="")
#f.close()
#Rewrite the program using the "with ..." statement. Then, check that the program works properly.

f = open("student_tw.txt")
for line in f:
    print(line, end="")
f.close()

print("----------------------")

with open("student_tw.txt") as file:
    for line in file:
        print(line, end="")