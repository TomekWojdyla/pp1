#17.	Find any text file on the Internet that contains at least 30 lines of text and download that file to your computer. Then, write a program that displays the first five lines from the file and then waits for the Enter key to be pressed. The program repeats displaying the next five lines from the file, waiting for the Enter key to be pressed each time.

file = open("Polska.txt", encoding="UTF-8")
#file_content = file.read()

count = 0
for line in file:
    count +=1
    print(line, end="")
    if count%5==0 and count>0:
        input("Press Enter to continue: ")

#print(file_content)

file.close()

            
            