# 39.	Write a program to separate even and odd numbers of a given array of integers. Put all even numbers first, and then odd numbers.

arr = [2,5,8,1,54,23,567,87,4,2,67]

n = len(arr)
for i in range(0,n-1):
    if arr[i]%2 == 0:
            pass
    else:
        for j in range(0,n-1):
            if arr[j]%2 == 0:
                pass
            else:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            
print(arr)