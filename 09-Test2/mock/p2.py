#(p2.py) An array contains at least 3 integers. All numbers in the array are equal except one. Create a function f(arr) that returns a number in the arr array that is different from the other numbers. Example:
#f([7,7,7,7,7,5,7,7])  5


def f(arr):
    lent = len(arr)
    first = arr[0]
    for i in range(1,lent):
        if arr[i-1]==arr[i]:
            pass
        else:
            if i==lent-1:
                return arr[i]
            elif arr[i]==arr[i+1]:
                return arr[i-1]
            else:
                return arr[i]

a = f([7,7,7,7,7,5,7,7])
print(a)
a = f([1,7,7,7,7,7,7,7])
print(a)
a = f([7,7,7,7,7,7,7,9])
print(a)
a = f([7,7,7,7,7,7,8,7])
print(a)
a = f([7,2,7,7,7,7,7,7])
print(a)