# 28.	Define a function compare(array1, array2) that returns True if both arrays are the same or False otherwise.  Two arrays are the same if they have the same number of elements and values of elements in cells of arrays with the same index are equal. Then create a program and try to compare the following arrays: 
#a.	["water","book","sky"]   ["water","book","sky"]
#b.	[True,False]   [True,False,True]
#c.	[5,3,1]   [5,3,1]
#d.	[3,2,1]   [3,2]

def compare(array1, array2):
    len1 = len(array1)
    len2 = len(array2)
    if len1 != len2:
        print("arrays not the same in length")
        check = False
    else:
        for i in range(len1):
            if array1[i] != array2[i]:
                print("arrays not the same in lenements")
                check = False
                break
            else:
                print("Arrays are the same")
                check = True
    return check

g = compare(["water","book","sky"],["water","book","sky"])
print(g)
g = compare([True,False],[True,False,True])
print(g)
g = compare([5,3,1],[5,3,1])
print(g)
g = compare([3,2,1],[3,2])
print(g)
    