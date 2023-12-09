#25.	An array contains values: 15, 8, 31, 47, 2, 19. Create a program that calculates and displays the array and the arithmetic mean of array values. Use the “while” loop statement.

array = [15,8,31,47,2,19]
i=0
sum = 0
while i<len(array):
    sum += array[i]
    i +=1
mean = sum/len(array)
print(mean)