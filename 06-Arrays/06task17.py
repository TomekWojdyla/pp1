#17.	An array contains values: [[0,0,0],[0,0,0],[0,0,0]]. Create a program that replaces the values of the main diagonal with 1. Use proper loop statements. Display the modified array. Sample result:
#1 0 0
#0 1 0
#0 0 1

array = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(0,len(array)):
    for j in range(0,len(array[0])):
        if i==j:
            array[i][j] = 1
        else:
            pass
    print (array[i])
