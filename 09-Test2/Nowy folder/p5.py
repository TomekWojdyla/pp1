def f(arr2D):
    lent = len(arr2D)
    counter = 0
    for i in range(lent):
        pow = arr2D[i][0]**2
        if arr2D[i][1]==pow:
            counter +=1
        else:
            pass
    return counter


