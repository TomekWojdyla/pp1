#9.	An array contains values: 2, 3, 7, 5, 4. Create a program that displays:
#a.	the array
#b.	number of elements
#c.	first value
#d.	second value
#e.	last value
#f.	last but one value (do not use negative index values)
#g.	sum of the first and last value
#h.	middle value
#i.	all array values separated by a single space (use a loop statement)
#Sample result:
#Array: [2,3,7,5,4]
#No. of elements: 5
#First value: 2
#Second value: 3
#…
#…
#Tip: to read the last value of an array:
#array[len(array)-1] or array[-1]


array = [2, 3, 7, 5, 4]

print(array)
print(len(array))
print(array[0])
print(array[1])
print(array[-1])
print(array[len(array)-2])
sum=array[0]+array[-1]
print(sum)
print(array[len(array)//2])
disp = ""
for item in array:
    disp += str(item) + " "
print(disp)
