#(p3.py) A two-dimensional array contains the same number of rows and columns. Create a function f(array2D) that, for the given two-dimensional array array2D, returns True when the sum of the values in each row of the array is equal to the sum of the values in the corresponding column (e.g., the sum of the values in row 3 is equal to the sum of the values in column 3) , and False otherwise. Example:
#f([[3,7,2],[4,2,5],[5,2,1]])  True
#f([[3,7,2],[4,2,5],[9,2,1]])  False

def f(array2D):
    check = False
    lent = len(array2D)
    sum_col = []
    sum_row = []
    for i in range(lent):
        sum = 0
        for j in range(lent):
            sum+=array2D[i][j]
        sum_row.append(sum)
    for i in range(lent):
        sum = 0
        for j in range(lent):
            sum+=array2D[j][i]
        sum_col.append(sum)
    if sum_col==sum_row:
        check = True
    return check

a = f([[3,7,2],[4,2,5],[5,2,1]])
print(a)
a = f([[3,7,2],[4,2,5],[9,2,1]])
print(a)