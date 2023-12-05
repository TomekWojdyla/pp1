#16.	An array contains values: [[3,9,2],[2,4,5],[7,1,6],[0,4,8]]. Create a program that calculates the sum of all odd numbers. Sample result:
#arr = [[3,9,2],[2,4,5],[7,1,6],[0,4,8]]
#sum_odd = 0
#for row in arr:
#    for element in row:
#        if …:
#            sum_odd = …
#print(…)


array = [[3,9,2],[2,4,5],[7,1,6],[0,4,8]]

sum_odd = 0
for i in range(0,len(array)):
    for j in range(0, len(array[0])):
        if array[i][j]%2 == 0:
            pass
        else:
            sum_odd += array[i][j]
            
print(sum_odd)

#lub

#sum_odd2 = 0
#for row in array:
#    for element in row:
#        if array[row][element]%2 == 0:
#            pass
#        else:
#            sum_odd2 += array[row][element]
            
#print(sum_odd2)