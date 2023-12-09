#24.	An array contains values: 15, 8, 31, 47, 2, 19. Create a program that calculates and displays the array and the arithmetic mean of array values. Use the “for” loop statement.

array = [15,8,31,47,2,19]

print(array)

sum = 0
for i in range(len(array)):
    sum += array[i]
mean = sum/len(array)
print(mean)