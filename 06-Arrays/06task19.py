# 19.	Try to create the following arrays. Then, display the created array content.
#a.	arr1 = [3,7,1,0,4]
#b.	arr2 = [[2,3],[7,1],[0,4]]
#c.	arr3 = [7 for i in range(5)]
#d.	arr4 = [i for i in range(1,10)]
#e.	arr5 = [i*2 for i in range(1,10)]
#f.	arr6 = [random.randint(1,20) for i in range(10)]
#g.	arr7 = [[] for i in range(5)]
#h.	arr8 = [[1 for i in range(2)] for j in range(4)]
#i.	arr9 = [[random.randint(1,20) for i in range(3)] for j in range(5)]
#j.	an array with values: 4,0,3
#k.	15-element array filled with zeros
#l.	an array with integer values in the range of <1,30>
#m.	20-element array filled with 0 or 1 randomly
#n.	two dimensional array with five rows and two columns filled with False

arr1 = [3,7,1,0,4]
print(arr1)
arr2 = [[2,3],[7,1],[0,4]]
print(arr2)
arr3 =[]
for i in range(5):
    arr3.append(7)
print(arr3)
arr4 =[]
for i in range(1,10):
    arr4.append(i)
print(arr4)
arr5 =[]
for i in range(1,10):
    arr5.append(i*2)
print(arr5)
arr6 =[]
import random
for i in range(1,10):
    arr6.append(random.randint(1,20))
print(arr6)
arr7 =[]
for i in range(5):
    arr7.append([])
print(arr7)
arr8 =[]
for i in range(4):
    arr8.append([])
    for j in range(2):
        arr8[i].append(1)
print(arr8)
arr9 =[]
for i in range(5):
    arr9.append([])
    for j in range(4):
        arr9[i].append(random.randint(1,20))
print(arr9)
arr10 = [4,0,3]
print(arr10)
arr11 = []
for i in range(15):
    arr11.append(0)
print(arr11)
arr12 = []
for i in range(1,30+1):
    arr12.append(i)
print(arr12)
arr13 = []
for i in range(0,15):
    arr13.append(random.randint(0,1))
print(arr13)
arr14 = []
for i in range(5):
    arr14.append([])
    for j in range(2):
        arr14[i].append(False)
print(arr14)

