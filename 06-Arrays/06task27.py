# 27.	An array contains integer numbers: 12, 6, 4, 9, 10. Create a program that displays the array values graphically as below. Define a function star(n) that returns the given number of asterisks as a string. Use a defined function in the program.
#12: ************
# 6: ******
# 4: ****
# 9: *********
#10: **********

array = [12,6,4,9,10]

def star(n):
    disp = ""
    for i in range(n):
        disp += "*"
    return disp

for i in range(len(array)):
    y = star(array[i])
    print(f"{array[i]}: {y}")
    
