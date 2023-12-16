def f(t):
    lent= len(t)
    import re
    arr = re.findall(r'[0-9]{1,}',t)
    lent2 = len(arr)
    sum = 0
    for i in range(lent2):
        sum +=int(arr[i])
    return sum



