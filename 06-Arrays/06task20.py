# 20.	An array contains integer numbers: 34,7,19,4,21,8. Create a program that calculates and displays the number of even values in the array. Use the ‘while’ loop statement.

array = [34,7,19,4,21,8]
z = len(array)
count = 0
i=0
while i<z:
    if array[i]%2 == 0:
        count +=1
    else:
        pass
    i += 1
print(count)