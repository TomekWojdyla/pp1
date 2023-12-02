# 10.	Find any text file on the Internet and download it to your computer. Then, write a program that displays its content.

file=open("skydiving.txt")
file_content = file.read()
print(file_content)
file.close()