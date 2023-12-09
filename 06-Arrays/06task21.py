#21.	An array contains natural numbers: 15, 8, 31, 47, 2, 19. Create a program that displays the contents of the array in reverse order. Use any loop statement. Sample result:
#existed array: 15 8 31 47 2 19 
#reverse array: 19 2 47 31 8 15

array = [15,8,31,47,2,19]
z = len(array)
for i in range(1,(z+1)//2+1):
    b=array[z-i]
    array[z-i] = array[i-1]
    array[i-1] = b
print(array)