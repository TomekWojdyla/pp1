#14.	An array contains values: [[2,5,4],[9,0,3]]. Create a program that displays:
#a.	the array
#b.	size of the array (number of rows and columns)
#c.	value 5 from the array
#d.	value 3 from the array
#e.	second row of the array as below:
#9 0 3
#Sample result:
#[[2,5,4],[9,0,3]]
#2 3
#5
#3
#9 0 3

array=[[2,5,4],[9,0,3]]
print(array)

rows=len(array)
columns=len(array[0])
print(f"Number of rows: {rows} and number of columns: {columns}")

m=array[0]
print(m[1])

m=array[1]
print(m[2])

n=array[1]
disp=""
for i in range(0,len(n)):
    disp += str(n[i]) + " "
print(disp)