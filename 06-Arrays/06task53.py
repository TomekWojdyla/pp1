#53.	In mathematics, a matrix is a rectangular array or table of numbers, symbols, or expressions, arranged in rows and columns, e.g.:
#-7  12 38
#41 -19 11
#Create a function identity_matrix(n) that returns an identity matrix (2D array) of size n (https://en.wikipedia.org/wiki/Identity_matrix). Then, create a function that displays a 2D array in rows and columns. Finally, create a program that displays three identity matrices with dimensions of 3, 5 and 8. Sample result:
#1 0 0 0 0
#0 1 0 0 0
#0 0 1 0 0
#0 0 0 1 0
#0 0 0 0 1

def identity_matrix(n):
    mat = []
    for i in range(n):
        col = []
        for j in range(n):
            if i==j:
                a = 1
            else:
                a=0
            col.append(a)
        mat.append(col)

    return mat

g = identity_matrix(5)
print(g)
