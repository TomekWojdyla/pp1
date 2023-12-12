# 46.	A two-dimensional array of size 2 by 4 contains integer numbers. Create a program that displays array values in rows and columns.

arr = [[2,3,4,5],[6,7,8,9]]

for i in range(2):
    disp = ""
    for j in range(4):
        disp += str(arr[i][j]) + " "
    print(disp)
    