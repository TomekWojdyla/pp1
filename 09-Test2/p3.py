def f(array2D):
    lent = len(array2D)
    a = array2D[0]
    high = len(a)
    
    sum_rows = []
    for i in range(lent):
        sum_row = 0
        for j in range(high):
            sum_row += array2D[i][j]
        sum_rows.append(sum_row)

    sum_cols = []
    for i in range(lent):
        sum_col = 0
        for j in range(high):
            sum_col += array2D[j][i]
        sum_cols.append(sum_col)

    if sum_cols == sum_rows:
        check = True
    else:
        check = False
    return check

if __name__ == "__main__":
    # function calls
    print(f([[3,7,2],[4,2,5],[5,2,1]]))
    print(f([[3,7,2],[4,2,5],[9,2,1]]))