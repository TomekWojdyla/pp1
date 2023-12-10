# 34.	Write a program that displays the tuple (10,20,30,40,50) in reverse order. Sample result:
#Tuple: 10,20,30,40,50
#Reverse order: 50,40,30,20,10

tuple1 = (10,20,30,40,50)
print(tuple1)
trans = list(tuple1)
for i in range(len(trans)//2):
    b=trans[len(trans)-i-1]
    trans[len(trans)-i-1] = trans[i]
    trans[i] = b
tuple1 = tuple(trans)
print(tuple1)