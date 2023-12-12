# 54.	Create a function transpose_matrix(m) that returns transposed matrix m:
# https://en.wikipedia.org/wiki/Transpose 

def transpose_matrix(x):
    rows = len(x)
    b = x[0]
    cols = len(b)
    
    x_trans = []
    x_t_col = []
    for i in range(rows):
        c = 0
        x_t_col.append(c)
    for i in range(cols):
        x_trans.append(x_t_col)
    
    y_trans = x_trans
    for j in range(cols):
        for i in range(rows):
            y_trans[j][i] = x[i][j]
    return y_trans

arr = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]

g = transpose_matrix(arr)
print(g)