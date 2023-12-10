# 42.	Define a function rand_elem(array) that returns a randomly selected array element. Using the function, display a few randomly selected array elements.

def rand_elem(arr):
    import random
    lent = len(arr)
    a = random.randint(0,lent-1)
    return arr[a]

n = int(input("Enter count of numbers: "))
array = [0,1,2,3,4,5,6,7,8,9,10]

for i in range(n):
    g = rand_elem(array)
    print(g)
    
    