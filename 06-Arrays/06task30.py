# 30.	Create a program that sorts elements of an array containing integer numbers. Apply the Bubble Sort sorting algorithm. Define a function bubblesort(array) that returns the sorted array. Try to sort and display any three arrays.

def bubblesort(arr):
    n = len(arr)
    # optimize code, so if the array is already sorted, it doesn't need
    # to go through the entire process
    swapped = False
    # Traverse through all array elements
    for i in range(n-1):
        # range(n) also work but outer loop will
        # repeat one time more than needed.
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] >arr[j+1]:
                swapped = True
                arr[j],arr[j+1] = arr[j+1],arr[j]
        if not swapped:
            # if we haven't needed to make a single swap, we 
            # can just exit the main loop.
            pass
    return arr
        
array_test = [64,34,25,12,22,11,90]
g = bubblesort(array_test)
print(g)

array_test = [5,3,1,2,3,2,1]
g = bubblesort(array_test)
print(g)

array_test = [5,3,-10,2,3,666,1]
g = bubblesort(array_test)
print(g)