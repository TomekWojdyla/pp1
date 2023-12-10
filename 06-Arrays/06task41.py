#41.	Write a program that checks whether the first array is a subset of the second one (whether all elements of the first array appear in the second array).

arr1 = [3]
arr2 = [5,4,3,2,1]

len1 = len(arr1)
len2 = len(arr2)
check = False
if len1>len2:
    print("arr1 is bigger than arr2")
else:
    for i in range(len1):
        check = False
        for j in range(len2):
            if arr1[i] == arr2[j]:
                check = True
                break
            else:
                pass
        if check == False:
            print("There is at least 1 number of arr1 not in arr2")
            break
        else:
            pass
if check == True:
    print("arr1 is a subset of arr2")
