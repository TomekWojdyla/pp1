def f(array2D):
    lent = len(array2D)
    for i in range(lent):
        sum_row = 0
        sums1 = []
        for j in range(lent):
            sum_row += array2D[i][j]
        sums1.append(sum_row)
    for i in range(lent):
        sum_col = 0
        sums2 = []
        for j in range(lent):
            sum_col += array2D[j][i]
        sums2.append(sum_col)   
    
    if sums1 == sums2:
        check = True
    else:
        check = False
    return check
    
g = f([[3,7,2],[4,2,5],[5,2,1]])
print(g)

g = f([[3,7,2],[4,2,5],[9,2,1]])
print(g)