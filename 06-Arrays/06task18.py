#18.	An array contains values: [[True,False],[True,True],[False,False]]. Create a program that changes values of an array to the opposite. Use a loop statement. Sample result:
#Before: [[True,False],[True,True],[False,False]]
#After:  [[False,True],[False,False],[True,True]]

array = [[True,False],[True,True],[False,False]]
print(array)

for row in array:
    for element in row:
        element = not element
        print(element)
#nie zapisuje do macierzy?? ale zamienia... czemu?
rint(array)

for i in range(0, len(array)):
    for j in range(0,len(array[0])):
        array[i][j] = not array[i][j]
        
print(array)