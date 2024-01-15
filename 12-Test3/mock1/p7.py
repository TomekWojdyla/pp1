#(p7.py) Create a function f(arr2D) that returns true when the sum of the values in at least two columns is the same. Otherwise, the function returns false. Example:
#arr = [[3,4,2],[2,2,2,0],[5,0,0,5],[4,7,0,2],[0,2,0,0]]
#f([[3,4,2],[5,1,6]])  True
#f([[3,4,2],[5,1,7]])  False
#f([[3,4],[5,1],[4,7]])  True
#f([[3,4],[5,9],[4,7]])  False

def f(arr2D):
    count_row = len(arr2D)
    count_col = len(arr2D[0])
    sums = []
    for i in range(count_col):
        sum_col = 0
        for j in range(count_row):
            sum_col +=arr2D[j][i]
        sums.append(sum_col)
    
    lent = len(sums)
    check = False
    for i in range(lent):
        for j in range(lent):
            if i==j:
                pass
            elif sums[i]==sums[j]:
                check = True
                break
    return check

a = f([[3,4,2],[5,1,6]])
print(a)
a=f([[3,4,2],[5,1,7]]) 
print(a)
a=f([[3,4],[5,1],[4,7]]) 
print(a)
a=f([[3,4],[5,9],[4,7]])
print(a)
                
