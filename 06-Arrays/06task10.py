#10.	An array contains values: 1, 2, 3, 4, 5. Create a program that modifies the array values. Display the array after each change.
#a.	subtract one from the first element of the array
#b.	increase the last array element by 4
#c.	multiple the middle array element by 2
#Sample result:
#Array: [1,2,3,4,5]
#Array: [0,2,3,4,5]
#Array: [0,2,3,4,9]
#Array: [0,2,6,4,9]

array = [1,2,3,4,5]
print(array)
array[0] = array[0] -1
print(f"Substract 1 from first element: {array}")

array[-1] +=4
print(f"Add 4 to last element: {array}")

mid = float(len(array)/2)
print(mid)
mid2 = len(array)//2
print(mid2)
array[int(mid)] = array[int(mid)]*2
print(f"Multiple middle element by 2: {array}")
