#15.	An array contains values: [[1,3,5],[8,7,2]]. Write a program that calculates and displays:
#a.	Sum of the first element in the first row and the last element in the last row
#b.	Sum of the elements in the middle column
#c.	Sum of the elements in the last row
#Sample result:
#3
#10
#7

array = [[1,4,5],[8,7,3]]

sum = array[0][0]+array[-1][-1]
print(sum)

sum2 = 0
for i in range(0, len(array)):
    sum2 += array[i][len(array[1])//2]
print(sum2)

sum3 = 0
for i in range(0,len(array[-1])):
    sum3 += array[-1][i]
print(sum3)