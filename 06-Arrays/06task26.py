# 26.	An array contains a list of Polish names: Genowefa, Onufry, Celestyna, Alojzy, Pankracy. Create a program that displays the longest name (consisting of the largest number of characters). Sample result:
#Names: Genowefa Onufry Celestyna Alojzy Pankracy
#Longest name: Celestyna

array = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]

disp = ""
max_len = 0
max_row = 0
for i in range(len(array)):
    disp += array[i]+ " "
    y = len(array[i])
    if y>max_len:
        max_len = y
        max_row = i
    else:
        pass
print(disp)
print(array[max_row])
            