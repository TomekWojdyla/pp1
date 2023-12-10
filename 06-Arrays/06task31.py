# 31.	Create a program that displays all unique elements in an array. Sample result:
#Array: 2 3 2 5 8 1 9 8
#Unique elements: 3 5 1 9

array = [2,3,2,5,8,1,7,31,3,9,8]
n = len(array)
unique = ""
for i in range(n):
    duplicate = False
    for j in range(n):
        if i == j:
            pass
        else:
            if array[i] == array[j]:
                duplicate = True
                break
            else:
                pass
    if duplicate == True:
        pass
    else:
        unique += str(array[i]) + " "
        
print(unique)
                