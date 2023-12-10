#bubble sorting
def bubble_sorting(arr):
    n = len(arr)
    swapped = False
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] >arr[j+1]:
                swapped = True
                arr[j],arr[j+1] = arr[j+1],arr[j]
        if not swapped:
            pass
    return arr

#a.	A function that returns the second largest element in an array
def second_largest(arr):
    arr_sorted = bubble_sorting(arr)
    value = arr_sorted[-2]
    return value

#b.	A function that returns the difference between the largest and smallest values in an array
def diff_lar(arr):
    arr_sorted = bubble_sorting(arr)
    value = arr_sorted[-1]-arr_sorted[0]
    return value

#c.	A function that returns the median of numbers in an array. Do not use built-in functions. The median is the middle value in the ordered sequence of numbers:
def arr_median(arr):
    value1 = arr[len(arr)//2]
    return value1

#array1 = [7,3,8,5,2]
#g = arr_median(array1)
#print(g)
#tego nie rozumiem? czemu przekazuje się posortowany?

#d d.	A function that returns a two-element array containing the smallest and largest values in an array

def min_max(arr):
    arr_sorted = bubble_sorting(arr)
    value = [arr_sorted[0],arr_sorted[-1]]
    return value
   
#e.	A function that returns array elements as a string, separated by the minus sign

def array_as_string(arr):
    value = ""
    n = len(arr)
    for i in range(n):
        value += str(arr[i])+"-"
    if value[-1] == "-":
        value = value[0:-1]
    return value
    
g = array_as_string([7,3,8,5,2])
print(g)