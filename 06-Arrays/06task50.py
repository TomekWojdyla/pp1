# 50.	An array contains integer numbers: [[-38, 19], [5,40],[-7,11],[29,16]]. Create a program that finds the smallest and largest values in the array and in which row and column they are located. 

arr = [[-38, 19], [5,40],[-7,-111],[29,16]]

min = arr[0][0]
for i in range(4):
    for j in range(2):
        if arr[i][j]<= min:
            min = arr[i][j]
        else:
            pass
for i in range(4):
    for j in range(2):
        if arr[i][j] ==min:
            a = i+1
            b = j+1
            break

print(min)
print(a)
print(b)

max = arr[0][0]
for i in range(4):
    for j in range(2):
        if arr[i][j]>= m:
            max = arr[i][j]
        else:
            pass
for i in range(4):
    for j in range(2):
        if arr[i][j] ==max:
            c = i+1
            d = j+1
            break
        
print(max)
print(c)
print(d)