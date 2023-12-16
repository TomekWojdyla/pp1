def f(arr):
    lent = len(arr)
    counter = len(arr)
    for i in range(lent):
        for j in range (lent):
            if  i==j:
                pass
            else:
                if arr[i]==arr[j]:
                    counter = counter -1
                    break
                else:
                    pass
    return counter

