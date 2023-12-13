# 19.	Find any text file on the Internet and download it to your computer. Then, write a program that copies the contents of this file to the copylines.txt file. Copy the contents of the file line by line. Finally, open both files in any text editor and check that their contents are the same.

file = open("skydiving.txt")
file2 = open("skydiving-copy.txt", "a")

for line in file:
    file2.write(line)
    
file.close()
file2.close()

