#48.	A function create_2d_arr(x,y) creates and returns two dimensional array with values of 0. Create a program and the function. Then create a two-dimensional array with dimensions of 3 by 5. Display the created array.

def create_2d_array(x,y):
    col = []
    for i in range(y):
        col.append(0)
    arr = []
    for i in range(x):
        arr.append(col)
    return 

g = create_2d_array(3,5)
print(g)