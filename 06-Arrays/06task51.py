# 51.	A two-dimensional array of the size 3 by 5 contains integer numbers. Create a program that swaps the first and the last row. Display array values in rows and columns before and after changes.

arr = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]

print (arr)

arr[0],arr[1], arr[2] = arr[2],arr[1],arr[0]

print(arr)