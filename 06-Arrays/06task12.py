#12.	An array contains integer numbers: [34,7,19,4,21,8]. Create a program that calculates and displays the number of even values in the array. Use the ‘for’ loop statement. Sample result:
#arr = [34,7,19,4,21,8]
#even = 0
#for a in arr:
#    if …:
#        even = even + 1
#print(…)

array=[34,7,19,4,21,8,2,8,66]
even_count = 0
for i in range(0,len(array)):
    if array[i]%2==0:
        even_count += 1
    else:
        pass
print(f"The count of even numbers is: {even_count}")

