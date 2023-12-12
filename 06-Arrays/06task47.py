# 47.	 A two-dimensional array contains the following numbers:
#7 3 7 9 0
#2 9 0 1 5
#3 8 6 4 7
#8 7 1 1 5
#Create a program that calculates the sum of values in the last column.

arr = [[7,3,7,9,0],[2,9,0,1,5],[3,8,6,4,7],[8,7,1,1,5]]

sum = 0
for i in range(4):
    for j in range(5):
        if j !=4:
            pass
        else:
            sum+= arr[i][j]
print(sum)
